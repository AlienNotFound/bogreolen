import { fetchGETRequest, fetchPOSTRequest, fetchPOSTImageRequest } from "$lib/api/common";
import { validateToken } from '$lib/server/auth.js';
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
        const listname = formData.get('listname');
        const token = await validateToken(cookies);

        try {
            const uploadData = new FormData();
            uploadData.append('file', image_file);

            const image_response = await fetchPOSTImageRequest<{ Error?: string, Success?: boolean, URL?: string}>('image', uploadData, token);

            const response = await fetchPOSTRequest<{ error?: string, message?: string}>('book', {
                title,
                author_name,
                image: image_response.URL,
                summary,
                year,
                category_title,
                listname
            }, token);

            return response.message;
            } catch (error) {
                if (error instanceof Error) {
                    return { error: error.message };
                }
            }
    }
}
export const load = async ({ cookies }) => {
    const token = await validateToken(cookies);
    try {
        const authors = await fetchGETRequest<Author[]>('authors', token);
        const categories = await fetchGETRequest<Catorgory[]>('categories', token);
        
        return { authors, categories }
    } catch (error) {
        return {
            authors: null,
            categories: null
        }
    }
}