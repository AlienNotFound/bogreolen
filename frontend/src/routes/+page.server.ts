import { redirect } from '@sveltejs/kit';
import { fetchGETRequest, fetchPOSTRequest } from '$lib/api/common.js';
import { createComment, editComment, deleteComment } from '$lib/actions/common.js';
import { validateToken } from '$lib/server/auth.js';

export const load = async ({ cookies }) => {
  const token: string | null = await validateToken(cookies) ?? null;

  if (!token) {
    throw redirect(302, '/login');
  }

  try {
    const tracks = await fetchTracks(token);
    const modalInfo = await fetchModalInfo(token);
    const reviews = await fetchGETRequest<Review[]>('reviews/user', token);

    return { reviews, tracks, modalInfo };
  } catch (error) {
    return { reviews: null };
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
    const modalInfo = await fetchGETRequest<TrackModal[]>('tracks/modal/user', token)
    
    return modalInfo;
  } catch (error) {
    console.error("Error loading modal info:", error);
    return [];
  }       
}

export const actions = {
  logout: async ({ cookies }) => {
    cookies.delete('access_token', { path: '/'});
    cookies.delete('refresh_token', { path: '/'});

    throw redirect(307, '/login');
  },
  track_book: async ({ request, cookies }) => {
    const formData = await request.formData();
    const book_id = formData.get('book_id');
    const current_page = formData.get('current_page');
    const last_page = formData.get('last_page'); 
    const token = await validateToken(cookies);

    try {
      const response = await fetchPOSTRequest<ResponseMessage<TrackModal[]>>('track/' + book_id, {
                read_today: true,
                current_page,
                last_page
            }, token);

          } catch (error) {
            if (error instanceof Error) {
        return { error: error.message };
      }
    }
  },
  create_comment: async ({ request, cookies }) => {
    const formData = await request.formData();
    const token = await validateToken(cookies);
    
    try {
      const response = await createComment(formData, token);
      return response;          
    } catch (error) {
      return { error: "An error occured."};
    }
  },
  edit_comment: async ({ request, cookies }) => {
    const formData = await request.formData();
    const token = await validateToken(cookies);
    
    try {
      const response = await editComment(formData, token);
      return response;
    } catch (error) {
      return { error: "An error occured..."};
    }
  },
  delete_comment: async ({ request, cookies }) => {
    const formData = await request.formData();
    const token = await validateToken(cookies);

    try {
      const response = await deleteComment(formData, token);
      return response;      
    } catch (error) {
      return { error: "An error occured."};
    }
  }
}