import type { PageServerLoad, Actions } from './$types';
import { redirect, fail } from '@sveltejs/kit';
import { fetchPOSTRequest } from '$lib/api/common';

export const actions: Actions = {
  default: async ({ request, cookies }) => {
    const formData = await request.formData();
    const username = formData.get('username');
    const password = formData.get('password');

    if (!username || !password) {
      return fail(400, {
        Error: 'Missing username or password'
      });
    }

    const response = await fetchPOSTRequest<{ access_token?: string | null}>('/login', {
        username,
        password
    })

    if (response.access_token) {
      const token = response.access_token;
      cookies.set('access_token', `${token}`, {
        httpOnly: true,
        path: '/',
        secure: false,
        sameSite: 'strict',
        maxAge: 60 * 60 * 24
      });

      throw redirect(307, "/");
    }
  }
};