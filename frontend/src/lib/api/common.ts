import { browser } from "$app/environment";
import { fail } from "@sveltejs/kit";
const LOCAL_API = 'http://localhost:8000/'
const DOCKER_API = 'http://backend:5000/'

export const API_BASE_URL = browser ? LOCAL_API : DOCKER_API;

export async function fetchGetRequestById<T>(route: string, id: string): Promise<T> {
    const response = await fetch(API_BASE_URL + route + id)
    const result: T = await response.json();
    // console.log(result);    
    return result
}

export async function fetchPOSTRequest<T>(route: string, body: any): Promise<T> {
    const response = await fetch(API_BASE_URL + route, {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
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
        throw new Error(message);
    }

    return result as T;
}

export async function fetchPUTRequest<T>(route: string, body: any): Promise<T> {
    const response = await fetch(API_BASE_URL + route, {
        method: 'PUT',
        body: JSON.stringify(body),
        headers: {
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
        throw new Error(message);
    }

    return result as T;
}