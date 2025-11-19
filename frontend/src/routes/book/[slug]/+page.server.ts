import { fetchGetRequestById, fetchPOSTRequest, fetchPUTRequest } from "$lib/api/common";
import { createComment } from "$lib/actions/common.js";
import { validateToken } from '$lib/server/auth.js';
import { fail } from "@sveltejs/kit";

export const actions = {
    add_to_list: async ({ request, cookies }) => {
        const formData = await request.formData();
        const book_id = formData.get('book_id');
        const listname = formData.get('listname');
        const token = await validateToken(cookies);

        try {
            const response = await fetchPOSTRequest<ResponseMessage<Book>>('add-to-list', {
                book_id,
                listname
            }, token);
                
            if (response?.Error == 'This book is already on a list!') {
                return fail(400, { success: false, duplicate_error: response?.Error });
            } else if (response?.Error) {
                return fail(400, { success: false, error: response?.Error });
            }
                
            } catch (error) {
                return { success: false, error: error.message };
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
            await fetchPOSTRequest<ResponseMessage<Review>>('review', {
                book_id,
                rating,
                reviewtext
            }, token)
    
        } catch (error) {
            if (error instanceof Error) {
                return fail(409, { error: error.message });
            }
        }
    },
    create_comment: async ({ request, cookies }) => {
        const formData = await request.formData();
        const token = await validateToken(cookies);
        
        try {
            await createComment(formData, token);      
        } catch (error) {
            if (error instanceof Error) {
                return fail(409, { comment_error: error.message })
            }
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