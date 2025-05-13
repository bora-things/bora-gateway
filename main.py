from fastapi import FastAPI, Request, Response
from dotenv import load_dotenv
import httpx
import os

load_dotenv(override=True)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8081")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:8082")

app = FastAPI()

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
async def proxy(full_path: str, request: Request):
    if full_path == "" or full_path == "/":
        target = FRONTEND_URL
    else:
        target = f"{BACKEND_URL}/{full_path}"

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=target,
            headers=dict(request.headers),
            content=await request.body(),
            timeout=30.0
        )

    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers)
    )
