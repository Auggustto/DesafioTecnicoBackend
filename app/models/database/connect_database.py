from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, session

# conexão db post local
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:2222/postgres"

# Descomentar quando rodar o up
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@postgres:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
db = SessionLocal()
