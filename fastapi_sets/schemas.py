from pydantic import BaseModel, EmailStr
from typing import Optional, List

# ------------
# Schemas senha
# ------------

class PasswordBase(BaseModel):
    login: str
    encrypted_password: str
    note: Optional[str] = None
    

class PasswordCreate(PasswordBase):
    pass 


class PasswordOut(PasswordCreate):
    id: int
    owner_id: int
    
    class Config:
        orm_mode: True
        
        
# ------------
# Schemas user
# ------------

class UsuarioBase(BaseModel):
    username: str
    email: EmailStr
    
    
class UsuarioCreate(UsuarioBase):
    password: str
    
    
class UsuarioOut(UsuarioBase):
    id: int
    passwords: List[PasswordOut] = []
    class Config:
        orm_mode: True
        