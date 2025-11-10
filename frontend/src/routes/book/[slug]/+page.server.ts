import { fetchGetRequestById, fetchPOSTRequest, fetchPUTRequest } from "$lib/api/common";
import { validateToken } from '$lib/server/auth.js';
import { fail } from "@sveltejs/kit";

export const actions = {
    add_to_list: async ({ request, cookies }) => {
        const formData = await request.formData();
        const book_id = formData.get('book_id');
        const listname = formData.get('listname');
        const token = await validateToken(cookies);

        try {
            const response = await fetchPOSTRequest<{ Error?: string, Success?: boolean}>('add-to-list', {
                book_id,
                listname
            }, token);
                
            if (response?.Error == 'This book is already on a list!') {
                return fail(400, { success: false, duplicate_error: response?.Error });
            } else if (response?.Error) {
                return fail(400, { success: false, error: response?.Error });
            }
                
            } catch (error) {
                return { success: false, error: "Failed to add book to list." };
            }
        },
    move_to_list: async ({ request, cookies }) => {
        const formData = await request.formData();
        const book_id = formData.get('book_id');
        const listname = formData.get('listname');
        const token = await validateToken(cookies);
        
        try {
            const response = await fetchPUTRequest<{ Error?: string, Success?: boolean}>('move-to-list/' + book_id, {
                listname
            }, token);

            if (response?.Error) {
                return fail(400, { success: false, error: response?.Error });
            }
        
        } catch (error) {
            return { success: false, error: "Failed to add book to list." };
        }
    },
    create_review: async ({ request, cookies }) => {
        const formData = await request.formData();
        const book_id = formData.get('book_id');
        const rating = formData.get('rating');
        const reviewtext = formData.get('reviewtext');
        const token = await validateToken(cookies);
         
        try {
            const response = await fetchPOSTRequest<{ Error?: string, Success?: boolean}>('review', {
                book_id,
                rating,
                reviewtext
            }, token)
            
            if (response?.Error == "Error: You've already reviewed this book") {
                return fail(40, { success: false, duplicate_error: response?.Error });
            } else if (response?.Error) {
                return fail(400, { success: false, error: response?.Error });
            }
        } catch (error: any) {
            if (error.message.includes("You've already reviewed this book")) {
                return fail(409, { success: false, duplicate_error: error.message });
            }
            return { success: false, error: "Failed to add review." };
        }
    },
    create_comment: async ({ request, cookies}) => {
        const formData = await request.formData();
        const review_id = formData.get('review_id');
        const comment_text = formData.get('comment_text');
        const token = await validateToken(cookies);
        
        try {
            const response = await fetchPOSTRequest<string>('comment', {
                review_id,
                comment_text
            }, token);

            // console.log(response)
            if (response == "Comment cannot be empty.") {
                return fail(400, {success: false, error: response})
            }
            return response;
            
        } catch (error) {
            return { error: "An error occured."}
        }
    }
}

export const load = async ({ params, cookies }) => {
    const token: string | null = await validateToken(cookies) ?? null;

    try {
        const book = await fetchGetRequestById<BookDetails>('book/', params.slug, token!);
        const status = await fetchGetRequestById<{book_status: string}>('book-status/', params.slug, token!);
        
        if (book.data && status.data) {
            return { 
                ...book.data,
                reviews: book.data.reviews ?? [],
                book_status: status.data.book_status
             }
        }
    } catch (error) {
        return {
            book: null,
            reviews: [],
            book_status: null
        }
    }
}