import type { H3Event, HTTPMethod } from "h3";
import { FetchError } from "ofetch";
const API_URL = "http://api.globalsafeips.com.co"

export default defineEventHandler(async (event) => {
    const route = event.context.params?._;
    const query = getQuery(event);
    const method: HTTPMethod = event.method;
    const requestHeaders = getHeaders(event);
    const token = getCookie(event, "token")


    const headers = {
        "Content-Type": requestHeaders["content-type"] || "application/json",
        "Accept": "application/json",
    } as any

    if(token) {
        headers["Authorization"] = `Bearer ${token}`
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
        console.log("Request", url, headers)
        const response = await $fetch(url, reqOpts);
        // console.log("Response", response)   
        return response;
    } catch (error) {
        console.log("Error", error)
        if (error instanceof FetchError) {
            setResponseStatus(event, error.statusCode);
            return error.data;
        }
        setResponseStatus(event, 500);
        return { error: JSON.stringify(error) };
    }
});
