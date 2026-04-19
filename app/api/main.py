from fastapi import FastAPI

app = FastAPI(title="vdm-safety-ai-agent", version="0.1.0")


@app.get("/")
def root() -> dict[str, str]:
    return {"service": "vdm-safety-ai-agent", "status": "ok"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
