import { json } from "@sveltejs/kit";
import { validateToken } from "$lib/server/auth";
import { API_BASE_URL } from "$lib/api/common.js";

export async function GET({ cookies, url, fetch }) {
    const token = await validateToken(cookies);
    const query = url.searchParams.get("query");

    if (!query) return json({ results: [] });

    const res = await fetch(`${API_BASE_URL}/search/${encodeURIComponent(query)}`, {
        headers: { Authorization: `Bearer ${token}` }
    });

    const data = await res.json();
    return json(data, { status: res.status });
}
