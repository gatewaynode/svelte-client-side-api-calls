/**
 * A simple get request API for the FastAPI server
 * 
 * @param {string} target - The target URL
 * @param {string} path - The path to the API endpoint
 * @param {string} params - The query string parameters 
 * @type {PromiseLike<{message: string}>} 
 * */
export async function get_stuff(
    target: string = "http://192.168.1.26:8000/",
    path: string = "",
    params: string = ""
): Promise<{ message: string }> {
    const response = await fetch(target + path + params);
    const payload = await response.json();
    return payload;
}

/**
 * A simple post request API for the FastAPI server
 * 
 * These parameters are positionally driven, so in order to pass a generic body 
 * in the function call, it must be the first parameter
 * 
 * @param {string} target - The target URL
 * @param {string} path - The path to the API endpoint
 * @param {string} body - The body of the request
 * @type {PromiseLike<{name: string, description: string, plu: number}>}
 */
export async function post_stuff(
    body = "",
    target = "http://192.168.1.26:8000",
    path = "/",
): Promise<{ name: string, description: string, plu: number }> {
    const response = await fetch(target + path, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: body
    });
    const payload = await response.json();
    return payload;
}

