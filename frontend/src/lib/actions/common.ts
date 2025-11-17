import { fetchPOSTRequest, fetchPUTRequest, fetchDELETERequest } from "$lib/api/common";
import { fail } from "@sveltejs/kit";

export async function createComment(formData: FormData, token: string) {
    const review_id = formData.get('review_id');
    const comment_text = formData.get('comment_text');

    const response = await fetchPOSTRequest<{error?:string}>('comment', {
        review_id,
        comment_text
    }, token)

    return response;
}

export async function editComment(formData: FormData, token: string) {
    const comment_id = formData.get('comment_id');
    const comment_text = formData.get('comment_text_edit');

    const response = await fetchPUTRequest<string>('comment/' + comment_id, {
        comment_text
    }, token)

    if (response == "Comment cannot be empty.") {
        return fail(400, {success: false, error: response})
    }
}

export async function deleteComment(formData: FormData, token: string) {
    const comment_id = formData.get('comment_id');

    const response = await fetchDELETERequest<string>('comment/' + comment_id, token)
        
    if (response == "Comment does not exist.") {
        return fail(400, {success: false, error: response})
    }
}