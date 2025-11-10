import { fetchPOSTRequest } from "$lib/api/common";
import { fail } from "@sveltejs/kit";

export async function createComment(formData: FormData, token: string) {
    const review_id = formData.get('review_id');
    const comment_text = formData.get('comment_text');

    const response = await fetchPOSTRequest<string>('comment', {
        review_id,
        comment_text
    }, token)

    if (response == "Comment cannot be empty.") {
        return fail(400, {success: false, error: response})
    }
}