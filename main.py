from fastapi import FastAPI
from fastapi import HTTPException
import sql

app = FastAPI()

@app.get("/")
async def root():
    return {"detail": "ok"}
    
@app.get("/createDB")
def create_db():
    sql.init_db()
    return {"Detail": "Banco criado"}