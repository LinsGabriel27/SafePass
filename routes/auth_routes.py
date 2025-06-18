from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_sets.schemas import UsuarioCreate, UsuarioOut, PasswordCreate, PasswordOut
from sql.database import get_db
from sql import crud

router = APIRouter()

@router.post("/users", response_model=UsuarioOut)
def criar_usuario(user: UsuarioCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/users/{user_id}", response_model=UsuarioOut)
def buscar_usuario(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_by_id(db, user_id)

@router.post("/users/{user_id}/passwords", response_model=PasswordOut)
def criar_senha(user_id: int, senha: PasswordCreate, db: Session = Depends(get_db)):
    return crud.create_password(db, user_id, senha)
