from fastapi import FastAPI
app = FastAPI(tittle="Importaciones API", version="0.1.0")

@app.get("/")
def root():
    return {"ok": True, "Service": "importaciones-api", "version": "0.1.0"}