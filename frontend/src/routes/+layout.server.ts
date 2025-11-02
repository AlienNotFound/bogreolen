import type { LayoutServerLoad } from './$types';
import { jwtDecode } from 'jwt-decode';

export const load: LayoutServerLoad = async ({ cookies }) => {
  const token = cookies.get('access_token');

  try {
    const user_id = jwtDecode(token!).sub;

    return { user_id };
  } catch (error) {
      console.error("Error getting user id", error);
      return null;
    }      
};