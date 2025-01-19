from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from db import Base


class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))