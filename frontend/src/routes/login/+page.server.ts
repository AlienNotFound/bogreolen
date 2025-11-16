import type {  Actions } from './$types';
import { redirect, fail } from '@sveltejs/kit';
import { fetchPOSTRequest } from '$lib/api/common';

export const actions: Actions = {
  default: async ({ request, cookies }) => {
    const formData = await request.formData();
    const username = formData.get('username');
    const password = formData.get('password');

    try {
      const response = await fetchPOSTRequest<{ access_token?: string | null, refresh_token?: string | null, errors?: Object | null}>('/login', {
          username,
          password
      })
  
      if (response.access_token) {
        const access_token = response.access_token;
        const refresh_token = response.refresh_token;
        cookies.set('access_token', `${access_token}`, {
          httpOnly: true,
          path: '/',
          secure: false,
          sameSite: 'strict',
          maxAge: 60 * 60
        });
  
        cookies.set('refresh_token', `${refresh_token}`, {
          httpOnly: true,
          path: '/',
          secure: false,
          sameSite: 'strict',
          maxAge: 60 * 60 * 24 * 7
        });
  
        throw redirect(307, "/");
      }
    } catch (error) {      
      if (error instanceof Error) {
        return { error: error.message }
      }
    }
  }
};