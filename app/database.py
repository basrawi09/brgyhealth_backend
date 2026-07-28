from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os


# Load .env
load_dotenv()


# Get database settings
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")


# MySQL Connection URL
DATABASE_URL = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)


print("DATABASE URL:", DATABASE_URL)



# Create Engine
engine = create_engine(
    DATABASE_URL,
    echo=True
)



# Create Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)



# Base Model
Base = declarative_base()



# Database Dependency
def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()