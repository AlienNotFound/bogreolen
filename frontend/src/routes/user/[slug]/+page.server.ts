import { fetchGetRequestById } from "$lib/api/common";
import { fail } from "@sveltejs/kit";

export const load = async ({ params, cookies }) => {
    const token = cookies.get('access_token');
    try {
        const user = await fetchGetRequestById<User>('user/', params.slug, token);
        const reviews = await fetchGetRequestById<Review[]>('reviews_by_user/', params.slug, token);
        const status = await fetchGetRequestById<BookDetails[]>('list_by_user/', params.slug, token);

        return { 
            ...user,
            reviews: reviews ?? [],
            books: status ?? [],
         }
    } catch (error) {
        console.error(error);        
        return {
            user: null,
            reviews: [],
            books: []
        }
    }
}