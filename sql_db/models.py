from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Task(Base):
    """
    Класс таска для использования в базе данных sql
    """
    __tablename__ = "tasks"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        comment="Уникальный идентификатор задачи",
    )
    task_text = Column(String, nullable=False, comment="Текст задачи")
    is_active = Column(
        Boolean,
        default=True,
        comment="Флаг активности задачи. True - задача активна. False - задача завершена",
    )
