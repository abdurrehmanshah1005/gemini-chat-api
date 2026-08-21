from fastapi import FastAPI

app = FastAPI(title="Gemini Chat API")


@app.get("/")
def root():
    return {"message": "Gemini Chat API"}


@app.get("/health")
def health():
    return {"status": "healthy"}
    