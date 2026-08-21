from fastapi import FastAPI, HTTPException
from google import genai
from pydantic import BaseModel

from app.config import settings

app = FastAPI(title="Gemini Chat API")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"message": "Gemini Chat API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/api/v1/chat")
def chat(request: ChatRequest):
    api_key = settings.GEMINI_API_KEY

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY is not configured",
        )

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=request.message,
    )

    return {
        "response": response.text,
    }