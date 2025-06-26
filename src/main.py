from fastapi import FastAPI, Request
import os
import httpx  
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

@app.post("/gemini")
async def proxy_to_gemini(request: Request):
    body = await request.json()

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{GEMINI_ENDPOINT}?key={GEMINI_API_KEY}",
            headers={"Content-Type": "application/json"},
            json=body
        )

    return response.json()
