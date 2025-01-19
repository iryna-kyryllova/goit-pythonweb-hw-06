from __future__ import annotations
from sqlalchemy import Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class Mark(Base):
    __tablename__ = "marks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mark: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[Date] = mapped_column(Date)

    student_id: Mapped[int] = mapped_column(ForeignKey('students.id'), nullable=False)
    student: Mapped[Student] = relationship('Student', back_populates="marks")

    subject_id: Mapped[int] = mapped_column(ForeignKey('subjects.id'), nullable=False)
    subject: Mapped[Subject] = relationship('Subject', back_populates="marks")