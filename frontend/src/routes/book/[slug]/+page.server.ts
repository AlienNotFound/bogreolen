import { fetchGetRequestById, fetchPOSTRequest, fetchPUTRequest } from "$lib/api/common";
import { fail } from "@sveltejs/kit";

export const actions = {
    add_to_list: async ({ request }) => {
        const formData = await request.formData();
        const bookid = formData.get('bookid');
        const listname = formData.get('listname');

        try {
            const response = await fetchPOSTRequest<{ Error?: string, Success?: boolean}>('add-to-list', {
                bookid,
                listname
            });
                
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
    move_to_list: async ({ request }) => {
        const formData = await request.formData();
        const bookid = formData.get('bookid');
        const listname = formData.get('listname');
        
        try {
            const response = await fetchPUTRequest<{ Error?: string, Success?: boolean}>('move-to-list/' + bookid, {
                listname
            });

            console.log(response)
    
            if (response?.Error) {
                return fail(400, { success: false, error: response?.Error });
            }
        
        } catch (error) {
            console.error(error);
            return { success: false, error: "Failed to add book to list." };
        }
    }
}

export const load = async ({ params }) => {
    try {
        const book = await fetchGetRequestById<BookDetails>('book/', params.slug);
        const status = await fetchGetRequestById<{book_status: string}>('book-status/', params.slug);

        
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