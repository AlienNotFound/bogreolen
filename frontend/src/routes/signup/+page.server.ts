import type { Actions } from './$types';
import { redirect } from '@sveltejs/kit';
import { fetchPOSTRequest } from '$lib/api/common';

export const actions: Actions = {
  default: async ({ request }) => {
    const formData = await request.formData();
    const username = formData.get('username');
    const email = formData.get('email');
    const password = formData.get('password');
    const password_again = formData.get('password_again');

    try {
      const response = await fetchPOSTRequest<ResponseMessage<User>>('/user', {
          username,
          email,
          password,
          password_again
      })
      
      if (response.message == "User created!") {
        redirect(303, "/login");
      }
    } catch(error) {
      if (error instanceof Error) {
        return { error: error.message }
      } else {
        throw error;
      }
    }
  }
};