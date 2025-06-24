from sqlalchemy import Column, Integer as Int, String as Str, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Int, primary_key=True, index=True)
    username = Column(Str, unique=True, nullable=False,index=True)
    hashd_password = Column(Str, nullable=False)
    email = Column(Str, nullable=False, index=True)

    passwords = relationship("Password", back_populates="owner", cascade="all, delete-orphan")

class Password(Base):
    __tablename__ = "passwords"

    id = Column(Int, primary_key=True, index=True)
    owner_id = Column(Int, ForeignKey("users.id"), nullable=False)
    login = Column(Str)
    encrypted_password = Column(Str, nullable=False)
    note = Column(Str)

    owner = relationship("User", back_populates="passwords")