from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)

    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'), nullable=False)
    group: Mapped["Group"] = relationship('Group', back_populates="students")

    marks: Mapped[list["Mark"]] = relationship('Mark', back_populates="students")
