import httpx
from fastapi import FastAPI, Request, Response

app = FastAPI()

ROUTING_TABLE = {
    "/server1": "http://localhost:4466",
    "/server2": "http://localhost:5566"
}

@app.middleware("http")
async def custom_reverse_proxy(request: Request, call_next):
    target_server = ROUTING_TABLE.get(request.url.path)
    if target_server is None:
        return await call_next(request)

    async with httpx.AsyncClient() as client:
        # headers = dict(request.headers)
        # params = dict(request.query_params)
        response = await client.request(
            request.method,
            target_server,
            # headers=headers,
            # params=params,
            data=await request.body()
        )

        proxy_response = Response(
            content=response.content,
            status_code=response.status_code,
            headers=response.headers,
        )

    return proxy_response

@app.get("/")
async def root():
    return {"message": "Custom Reverse Proxy mit FastAPI"}
