import { fetchGetRequestById, fetchPOSTRequest, fetchPUTRequest } from "$lib/api/common";
import { fail } from "@sveltejs/kit";

export const actions = {
    add_to_list: async ({ request, cookies }) => {
        const formData = await request.formData();
        const bookid = formData.get('bookid');
        const listname = formData.get('listname');
        const token = cookies.get('access_token');

        try {
            const response = await fetchPOSTRequest<{ Error?: string, Success?: boolean}>('add-to-list', {
                bookid,
                listname
            }, token);
                
            if (response?.Error == 'This book is already on a list!') {
                return fail(400, { success: false, duplicate_error: response?.Error });
            } else if (response?.Error) {
                return fail(400, { success: false, error: response?.Error });
            }
                
            } catch (error) {
                console.error(error);
                return { success: false, error: "Failed to add book to list." };
            }
        },
    move_to_list: async ({ request, cookies }) => {
        const formData = await request.formData();
        const bookid = formData.get('bookid');
        const listname = formData.get('listname');
        const token = cookies.get('access_token');
        
        try {
            const response = await fetchPUTRequest<{ Error?: string, Success?: boolean}>('move-to-list/' + bookid, {
                listname
            }, token);

            console.log(response)
    
            if (response?.Error) {
                return fail(400, { success: false, error: response?.Error });
            }
        
        } catch (error) {
            console.error(error);
            return { success: false, error: "Failed to add book to list." };
        }
    },
    create_review: async ({ request, cookies }) => {
        const formData = await request.formData();
        const bookid = formData.get('bookid');
        const rating = formData.get('rating');
        const reviewtext = formData.get('reviewtext');
        const token = cookies.get('access_token');

        try {
            const response = await fetchPOSTRequest<{ Error?: string, Success?: boolean}>('review', {
                bookid,
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
    }
}

export const load = async ({ params, cookies }) => {
    const token = cookies.get('access_token');
    try {
        const book = await fetchGetRequestById<BookDetails>('book/', params.slug, token);
        const status = await fetchGetRequestById<{book_status: string}>('book-status/', params.slug, token);
        
        return { 
            ...book,
            reviews: book.reviews ?? [],
            book_status: status.book_status
         }
    } catch (error) {
        console.error(error);        
        return {
            book: null,
            reviews: [],
            book_status: null
        }
    }
}