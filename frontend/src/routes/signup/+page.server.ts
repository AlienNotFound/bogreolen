import type { Actions } from './$types';
import { redirect, fail } from '@sveltejs/kit';
import { fetchPOSTRequest } from '$lib/api/common';

export const actions: Actions = {
  default: async ({ request }) => {
    const formData = await request.formData();
    const username = formData.get('username');
    const email = formData.get('email');
    const password = formData.get('password');
    const password_again = formData.get('password_again');

    if (!username || !email || !password || !password_again) {
      return fail(400, {
        Error: 'Missing username, email or password'
      });
    }

    const response = await fetchPOSTRequest<string | object | null>('/user', {
        username,
        email,
        password,
        password_again
    })

    if (Object.values(response!)[0] == "User created!") {
      throw redirect(307, "/login");
    } else {
      return {Error: response}      
    }
  }
};