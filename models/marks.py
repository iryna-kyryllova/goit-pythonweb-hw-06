from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base
from models.students import Student
from models.subjects import Subject


class Mark(Base):
    __tablename__ = "marks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mark: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[Date] = mapped_column(Date)

    student_id: Mapped[Student] = relationship('Student', back_populates="marks")
    subject_id: Mapped[Subject] = relationship('Subject', back_populates="marks")