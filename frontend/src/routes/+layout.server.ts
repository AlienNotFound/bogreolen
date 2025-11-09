import { validateToken } from '$lib/server/auth.js';
import type { LayoutServerLoad } from './$types';
import { jwtDecode } from 'jwt-decode';
import { redirect } from '@sveltejs/kit';

export const load: LayoutServerLoad = async ({ cookies }) => {
  const token: string | null = await validateToken(cookies) ?? null;

  if (!token) {
      if (!token) {
      throw redirect(302, '/login');
    }
  }

  try {
    let user_id: string | undefined;
    if (token) {
      user_id = jwtDecode(token).sub;
    }

    return { user_id };
  } catch (error) {
      console.error("Error getting user id", error);
      return { user_id: null, token: null };
    }      
};