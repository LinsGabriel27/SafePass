from sqlalchemy.orm import Session
from sql.models import User, Password
from fastapi_sets.schemas import UsuarioCreate, PasswordCreate
from passlib.hash import bcrypt

# Criar usuário
def create_user(db: Session, user: UsuarioCreate):
    hashed_pw = bcrypt.hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashd_password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Buscar usuário por ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Criar senha
def create_password(db: Session, user_id: int, senha: PasswordCreate):
    db_senha = Password(
        owner_id=user_id,
        login=senha.login,
        encrypted_password=senha.encrypted_password,
        note=senha.note
    )
    db.add(db_senha)
    db.commit()
    db.refresh(db_senha)
    return db_senha
