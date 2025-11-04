import { validateToken } from '$lib/server/auth.js';
import type { LayoutServerLoad } from './$types';
import { jwtDecode } from 'jwt-decode';

export const load: LayoutServerLoad = async ({ cookies }) => {
  const token: string | null = await validateToken(cookies) ?? null;

  try {
    let user_id: string | undefined;
    if (token) {
      user_id = jwtDecode(token).sub;
    }

    return { user_id, token };
  } catch (error) {
      console.error("Error getting user id", error);
      return { user_id: null, token: null };
    }      
};