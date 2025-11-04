import { fetchGETRequest, fetchPUTRequest } from '$lib/api/common';

export const load = async ({ cookies }) => {
    const token = cookies.get('access_token');
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
    const token = cookies.get('access_token');

    try {
      const response = await fetchPUTRequest<{ Error?: string, Success?: boolean}>('track/' + track_id, {
                read_today: true,
                current_page,
                last_page,
                date
            }, token);

            console.log(response)
    } catch (error) {
      console.error(error);
      return { success: false, error: "Failed to update track." };
    }
  }
}