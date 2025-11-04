import { fetchGetRequestById } from "$lib/api/common";

export const load = async ({ params, parent }) => {
    const { token } = await parent();
    try {
        const user = await fetchGetRequestById<User>('user/', params.slug, token!);
        const reviews = await fetchGetRequestById<Review[]>('reviews_by_user/', params.slug, token!);
        const status = await fetchGetRequestById<BookDetails[]>('list_by_user/', params.slug, token!);

        return { 
            ...user.data,
            reviews: reviews.data ?? [],
            books: status.data ?? [],
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