import { redirect, fail } from '@sveltejs/kit';
import { fetchGetRequestById, fetchPUTRequest } from '$lib/api/common.js';
import { jwtDecode } from 'jwt-decode';

export const load = async ({ cookies }) => {
  const token = cookies.get('access_token');
  if (!token) {
    throw redirect(302, '/login');
  }

  try {
    const user_id = jwtDecode(token!).sub;

    if (user_id) {
        const user = await fetchGetRequestById<User>('user/', user_id, token);
        return { ...user };
    }

  } catch (error) {
    fail(500)
      console.error("Error loading user:", error);
      return { user: null };
    }      
};

export const actions = {
  edit_user: async ({ request, cookies }) => {
    const token = cookies.get('access_token');
    const formData = await request.formData();
    const user_id = jwtDecode(token!).sub;
    const username = formData.get('username');
    const email = formData.get('email'); 
    const password = formData.get('password'); 
    const password_again = formData.get('password_again'); 
    const current_password = formData.get('current_password'); 

    try {
        const response = await fetchPUTRequest<{ Error: string, Success: string }>('user/' + user_id, {
                username,
                email,
                password,
                password_again,
                current_password
            }, token);
        console.log(response)
        return response
    } catch (error) {
        if (error instanceof Error) {
            return { success: false, error: error.message };
        }
    }
  }
}