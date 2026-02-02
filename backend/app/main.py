from fastapi import FastAPI

app = FastAPI(title="Blog Post Helper API")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
