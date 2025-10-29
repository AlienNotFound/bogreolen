export const API_BASE_URL = 'http://localhost:8000/'

export async function fetchGetRequestById<T>(route: string, id: string): Promise<T> {
    const response = await fetch(API_BASE_URL + route + id)
    const result: T = await response.json();
    console.log(result);
    return result
}

export async function fetchPostRequest<T>(route: string, body: any): Promise<T> {
    const response = await fetch(API_BASE_URL + route, {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    const result: T = await response.json();
    console.log(result);
    return result
}