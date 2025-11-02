import { fetchGETRequest } from '$lib/api/common';

export const load = async ({ cookies }) => {
    const token = cookies.get('access_token');
    try {
        const tracks = await fetchGETRequest<Track[]>('tracks/user', token);
        console.log("tracks", tracks)

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