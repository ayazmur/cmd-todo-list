import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
from os import getenv

load_dotenv('ci/.env')
DATABASE_URL = f"postgresql+psycopg2://{getenv("POSTGRES_USER")}:{getenv("POSTGRES_PASSWORD")}@{getenv("POSTGRES_HOST")}:{getenv("POSTGRES_PORT")}/{getenv("POSTGRES_DB")}"

engine = db.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
