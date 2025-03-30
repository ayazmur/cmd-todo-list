import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cached_property
from dataclasses import dataclass


class DBSettings(BaseSettings):
    SCHEMA: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    DB_TYPE: str

    @cached_property
    def get_database_url(self) -> str:
        dsn = PostgresDsn(
            f"{self.SCHEMA}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
        return str(dsn)

    model_config = SettingsConfigDict(env_file=Path("ci/.env"))


db_settings = DBSettings()
engine = db.create_engine(db_settings.get_database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
