import { fetchGetRequestById } from "$lib/api/common";
import { API_BASE_URL } from "$lib/api/common";
import { jwtDecode } from "jwt-decode";

export async function validateToken(cookies: any) {
    const access_token = cookies.get('access_token') ?? null;
    const refresh_token = cookies.get('refresh_token') ?? null;
    
    if (!access_token) {
        return null;
    }
    
    const user_id: string = jwtDecode(access_token).sub!
    const response = await fetchGetRequestById<ResponseMessage<User>>('user/', user_id, access_token);

    if (response.status == 200) {
        return access_token;
    }

    if (response.msg == "Token has expired")
    {
        const refresResponse = await fetchRefreshToken(refresh_token);
        console.log("refresResponse", refresResponse)

        if (refresResponse.ok) {
        const { access_token: newAccessToken } = await refresResponse.json();
        console.log(refresResponse)
        cookies.set('access_token', newAccessToken, { path: "/"});

        return newAccessToken
        } 
    }
}

export async function fetchRefreshToken(refresh_token: string) {
    return await fetch(API_BASE_URL + "refreshtoken", {
        method: 'Post',
        credentials: 'include',
        headers: {
            'Authorization': `Bearer ${refresh_token}`,
        }
    });
}