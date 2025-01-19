from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    teacher_id: Mapped[int] = mapped_column(ForeignKey('teachers.id'), nullable=False)
    teacher: Mapped["Teacher"] = relationship('Teacher', back_populates="subjects")

    mark: Mapped[list["Mark"]] = relationship('Mark', back_populates="subjects")