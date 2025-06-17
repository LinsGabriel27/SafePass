from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
async def root():
    try:
        return {"detail": "ok"}
    except ValueError:
        raise HTTPException(status_code=500, detail="Erro desconhecido")
    
