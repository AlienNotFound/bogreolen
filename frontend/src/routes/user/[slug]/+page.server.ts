import { fetchGetRequestById } from "$lib/api/common";
import { createComment } from "$lib/actions/common";
import { validateToken } from "$lib/server/auth";
import { fail } from "@sveltejs/kit";

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

export const actions = {
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