import type { Cookies } from '@sveltejs/kit';

export const actions = {
    login: async ({ cookies: Cookies }) => {
        const userid = 1;

        const token_payload = {
            userId: userid
        }

        const access_token = token_payload.userId.toString();

        Cookies.set("access_token", access_token, {
            path: "/"
        });
    }
}