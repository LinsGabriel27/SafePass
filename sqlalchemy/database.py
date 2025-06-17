from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

database_url = "sqlite:///meubanco.db"

engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)