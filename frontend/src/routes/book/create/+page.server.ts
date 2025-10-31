import { fetchGETRequest, fetchPOSTRequest, fetchPUTRequest, fetchPOSTImageRequest } from "$lib/api/common";
import { fail } from "@sveltejs/kit";

export const actions = {
    create_book: async ({ request, cookies }) => {
        const formData = await request.formData();
        const title = formData.get('title');
        const author_name = formData.get('author_name');
        const image_file = formData.get('image') as File;
        const summary = formData.get('summary');
        const year = formData.get('year');
        const category_title = formData.get('category_title');
        const book_status = formData.get('book_status');
        const token = cookies.get('access_token');

        try {
            const uploadData = new FormData();
            uploadData.append('file', image_file);

            const image_response = await fetchPOSTImageRequest<{ Error?: string, Success?: boolean, URL?: string}>('image', uploadData, token);

            console.log(image_response.URL)
            const response = await fetchPOSTRequest<{ Error?: string, Success?: boolean}>('book', {
                title,
                author_name,
                image: image_response.URL,
                summary,
                year,
                category_title,
                book_status
            }, token);
                
            if (response?.Error == 'This book is already exists!') {
                return fail(400, { success: false, duplicate_error: response?.Error });
            } else 
            if (response?.Error) {
                return fail(400, { success: false, error: response?.Error });
            }
                
            } catch (error) {
                console.error(error);
                return { success: false, error: "Failed to add book to list." };
            }
    }
}
export const load = async ({ cookies }) => {
    const token = cookies.get('access_token');
    try {
        const authors = await fetchGETRequest<{author: string}>('authors', token);
        
        return { authors }
    } catch (error) {
        console.error(error);        
        return {
            authors: null
        }
    }
}