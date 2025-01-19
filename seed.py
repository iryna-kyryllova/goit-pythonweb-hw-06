from faker import Faker
from random import randint
from datetime import date
from db import session
from models import Group
from models import Student
from models import Teacher
from models import Subject
from models import Mark

fake = Faker('uk_UA')

GROUPS = ['Group 1', 'Group 2', 'Group 3']
SUBJECTS = ['Math', 'Python', 'React', 'CSS', 'HTML', 'JavaScript', 'SQL', 'Django', 'Flask', 'FastAPI']
STUDENTS_COUNT = 40
TEACHERS_COUNT = 5

def seed_groups(groups: list) -> None:
    for group in groups:
        new_group = Group(name=group)
        session.add(new_group)
    session.commit()

def seed_students(students: int) -> None:
    group_ids = [x.id for x in session.query(Group).all()]

    for i in range(students):
        new_student = Student(
            name=fake.name(),
            email=fake.email(),
            group_id=fake.random_element(group_ids)
        )
        session.add(new_student)
    session.commit()

def seed_teachers(teachers: int) -> None:
    for i in range(teachers):
        new_teacher = Teacher(
            name=fake.name(),
        )
        session.add(new_teacher)
    session.commit()

def seed_subjects(subjects: list) -> None:
    teacher_ids = [x.id for x in session.query(Teacher).all()]

    for subject in subjects:
        new_subject = Subject(name=subject, teacher_id=fake.random_element(teacher_ids))
        session.add(new_subject)
    session.commit()

def seed_marks() -> None:
    subject_ids = [x.id for x in session.query(Subject).all()]
    student_ids = [x.id for x in session.query(Student).all()]
    start_date = date(2024, 1, 1)
    end_date = date(2025, 1, 1)

    for subject in subject_ids:
        for student in student_ids:
            new_mark = Mark(
                mark=randint(1, 12),
                created_at=fake.date_between_dates(date_start=start_date, date_end=end_date),
                student_id=student,
                subject_id=subject
            )
            session.add(new_mark)
    session.commit()

if __name__ == '__main__':
    seed_groups(GROUPS)
    seed_students(STUDENTS_COUNT)
    seed_teachers(TEACHERS_COUNT)
    seed_subjects(SUBJECTS)
    seed_marks()