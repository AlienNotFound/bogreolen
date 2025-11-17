import { fetchGETRequest, fetchPUTRequest } from '$lib/api/common';
import { validateToken } from '$lib/server/auth.js';
import { fail } from '@sveltejs/kit';

export const load = async ({ cookies }) => {
    const token = await validateToken(cookies);
    try {
        const tracks = await fetchGETRequest<Track[]>('tracks/user', token);

        return { 
            tracks: tracks ?? []
         }
    } catch (error) {
        console.error(error);        
        return {
            tracks: []
        }
    }
}

export const actions = {
  edit_track: async ({ request, cookies }) => {
    const formData = await request.formData();
    const track_id = formData.get('track_id');
    const current_page = formData.get('current_page');
    const last_page = formData.get('last_page'); 
    const date = formData.get('date'); 
    const token = await validateToken(cookies);

    try {
      const response = await fetchPUTRequest<ResponseMessage<Track>>('track/' + track_id, {
                read_today: true,
                current_page,
                last_page,
                date
            }, token);

      return response;

    } catch (error) {
      if (error instanceof Error) {
        return fail(409, {error: error.message });
      }
    }
  }
}