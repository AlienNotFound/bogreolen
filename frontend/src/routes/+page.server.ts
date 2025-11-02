import { redirect } from '@sveltejs/kit';
import { fetchGETRequest, fetchPOSTRequest } from '$lib/api/common.js';

export const load = async ({ cookies }) => {
  const token = cookies.get('access_token');
  if (!token) {
    throw redirect(302, '/login');
  }

  try {
    const tracks = await fetchTracks(token);
    const modalInfo = await fetchModalInfo(token);
    const reviews = await fetchGETRequest<Review[]>('reviews/user', token);
    return { reviews, tracks, modalInfo };
  } catch (error) {
      console.error("Error loading reviews:", error);
      return [];
    }      
};
    
async function fetchTracks(token: string) {
  try {
    const tracks = await fetchGETRequest<Track[]>('tracks/user', token);    
    return tracks;
  } catch (error) {
    console.error("Error loading tracks:", error);
    return [];
  }
}

async function fetchModalInfo(token: string) {
  try {
    const modalInfo = await fetchGETRequest<Book[]>('tracks/modal/user', token)
    return modalInfo;
  } catch (error) {
    console.error("Error loading modal info:", error);
    return [];
  }       
}

export const actions = {
  logout: async ({ cookies }) => {
    cookies.delete('access_token', { path: '/'});

    throw redirect(307, '/login');
  },
  track_book: async ({ request, cookies }) => {
    const formData = await request.formData();
    const book_id = formData.get('book_id');
    const current_page = formData.get('current_page');
    const last_page = formData.get('last_page'); 
    const token = cookies.get('access_token');

    try {
      const response = await fetchPOSTRequest<{ Error?: string, Success?: boolean}>('track/' + book_id, {
                read_today: true,
                current_page,
                last_page
            }, token);

            console.log(response)
    } catch (error) {
      console.error(error);
      return { success: false, error: "Failed to track book." };
    }
  }
}