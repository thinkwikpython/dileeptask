from databases import Database
from models import Base
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker, Session



DATABASE_URL = "postgresql://postgres:dileep77@localhost:5432/aaa3"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()  # You should replace this with your actual method of getting a database session
    try:
        yield db
    finally:
        db.close()