const PROD_API = import.meta.env.VITE_API_BASE_URL

export const API_BASE_URL = "https://bogreolen.onrender.com/";
export async function fetchGetRequestById<T>(route: string, id: string, token: string = ""): Promise<ResponseMessage<T>> {
    const headers: Record<string, string> = {};
    if (token) headers['Authorization'] = `Bearer ${token}`;

    const response = await fetch(API_BASE_URL + route + id, {
        method: 'GET',
        headers,
        credentials: 'include'
    })

    const result: T = await response.json();
    return {
        status: response.status,
        data: result
    }
}

export async function fetchGETRequest<T>(route: string, token: string = ""): Promise<T> {
   const headers: Record<string, string> = {};
    if (token) headers['Authorization'] = `Bearer ${token}`;
    
    const response = await fetch(API_BASE_URL + route, {
        method: 'GET',
        headers,
        credentials: 'include'
    })
    
    const result: T = await response.json();
    return result
}

export async function fetchPOSTRequest<T>(route: string, body: any, token: string = ""): Promise<T> {
    const response = await fetch(API_BASE_URL + route, {
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify(body),
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    })

    let result: any;

    try {
        result = await response.json()
    } catch {
        result = null;
    }

    if (!response.ok) {
        const message = result?.Error || result?.Message || 'Unknown error';
        return message;
    }

    return result as T;
}

export async function fetchPOSTImageRequest<T>(route: string, body: any, token: string = ""): Promise<T> {
    const response = await fetch(API_BASE_URL + route, {
        method: 'POST',
        credentials: 'include',
        body: body,
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })

    let result: any;

    try {
        result = await response.json()
    } catch {
        result = null;
    }

    if (!response.ok) {
        const message = result?.Error || result?.message || 'Unknown error';
        throw new Error(message);
    }

    return result as T;
}

export async function fetchPUTRequest<T>(route: string, body: any, token: string = ""): Promise<T> {
    const response = await fetch(API_BASE_URL + route, {
        method: 'PUT',
        credentials: 'include',
        body: JSON.stringify(body),
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    })
    
    let result: any;

    try {
        result = await response.json()
    } catch {
        result = null;
    }
    
    if (!response.ok) {
        const message = result?.Error || result?.message || 'Unknown error';
        return message
    }
    
    return result as T;
}

export async function fetchDELETERequest<T>(route: string, token: string = ""): Promise<T> {
    const response = await fetch(API_BASE_URL + route, {
        method: 'DELETE',
        credentials: 'include',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    })
    
    let result: any;

    try {
        result = await response.json()
    } catch {
        result = null;
    }
    
    if (!response.ok) {
        const message = result?.Error;
        return message;
    }
    
    return result as T;
}