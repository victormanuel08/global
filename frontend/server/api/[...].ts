import type { H3Event, HTTPMethod } from "h3";
import { FetchError } from "ofetch";

export default defineEventHandler(async (event) => {
    const route = event.context.params?._;
    const query = getQuery(event);
    const method: HTTPMethod = event.method;
    const requestHeaders = getHeaders(event);
    const headers = {
        "Content-Type": requestHeaders["content-type"] || "application/json",
        "Accept": "application/json",
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
        let url = `http://localhost:8000/${route}/`;
        const response = await $fetch(url, reqOpts);
        return response;
    } catch (error) {
        if (error instanceof FetchError) {
            setResponseStatus(event, error.statusCode);
            return error.data;
        }
        setResponseStatus(event, 500);
        return { error: JSON.stringify(error) };
    }
});
