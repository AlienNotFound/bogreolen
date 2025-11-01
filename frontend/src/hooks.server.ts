import type { Handle } from '@sveltejs/kit';
import { redirect } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	if (event.url.pathname.startsWith('/custom')) {
		return new Response('custom response');
	}

    const token = event.cookies.get('access_token');
    if (!token && event.url.pathname != "/login" && event.url.pathname != "/signup") {
        console.log(token)
        throw redirect(302, '/login');
    }

	const response = await resolve(event);
	return response;
};