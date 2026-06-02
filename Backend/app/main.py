from fastapi import FastAPI

app = FastAPI(title="Smart Interview Analyzer API")

@app.get("/health")
def health():
    return {"status": "ok"}
