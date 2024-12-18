import type { H3Event, HTTPMethod } from "h3";
import { FetchError } from "ofetch";
const API_URL = "https://api.globalsafeips.com.co"
//const API_URL = "http://localhost:8000"

export default defineEventHandler(async (event) => {
    const route = event.context.params?._;
    const query = getQuery(event);
    const method: HTTPMethod = event.method;
    const requestHeaders = getHeaders(event);
    const token = getCookie(event, "token");
    const refreshToken = getCookie(event, "refresh_token");

    const headers = {
        "Content-Type": requestHeaders["content-type"] || "application/json",
        "Accept": "application/json",
    } as any;

    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }

    const reqOpts: Record<string, unknown> = {
        method,
        headers,    
        query,
    };

    if (["POST", "PUT", "PATCH"].includes(method)) {
        if (headers["Content-Type"] === "application/json") {
          reqOpts.body = await readBody(event);
        } else {
          reqOpts.body = await readRawBody(event, false);
        }
    }

    try {
        let url = `${API_URL}/${route}/`;
      
        const response = await $fetch(url, reqOpts);
        return response;
    } catch (error) {
      
        if (error instanceof FetchError) {
            setResponseStatus(event, error.statusCode);
            if (error.statusCode === 401 && refreshToken) {
                // Si el token ha expirado, intenta refrescarlo
                const refreshed = await refreshAccessToken(refreshToken);
                if (refreshed) {
                 
                    // Reintenta la solicitud con el nuevo token
                    headers["Authorization"] = `Bearer ${refreshed.accessToken}`;
                    const retryResponse = await $fetch(url, reqOpts);
                    return retryResponse;
                }
            }
            return error.data;
        }
        setResponseStatus(event, 500);
        return { error: JSON.stringify(error) };
    }
});

const refreshAccessToken = async (refreshToken: string) => {
    try {
        const response = await $fetch('/api/auth/refresh', {
            method: 'POST',
            body: { refreshToken },
        });
      
        return response;
    } catch (error) {
       
        return null;
    }
};
