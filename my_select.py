from sqlalchemy import func, desc
from db import session
from models import Group
from models import Student
from models import Teacher
from models import Subject
from models import Mark

def select_1():
    result = (
        session.query(
            Student.id,
            Student.name,
            func.avg(Mark.mark).label('avg_mark')
        )
        .join(Mark, Student.id == Mark.student_id)
        .group_by(Student.id, Student.name)
        .order_by(desc('avg_mark'))
        .limit(5)
        .all()
    )
    for student in result:
        print(f"ID: {student.id}, Name: {student.name}, Avg Mark: {student.avg_mark:.2f}")

def select_2(subject_id: int):
    result = (
        session.query(
        Student.id,
        Student.name,
        func.avg(Mark.mark).label('avg_mark')
        )
        .join(Mark, Student.id == Mark.student_id)
        .filter(Mark.subject_id == subject_id)
        .group_by(Student.id, Student.name)
        .order_by(desc('avg_mark'))
        .limit(1)
        .first()
    )
    print(f"ID: {result.id}, Name: {result.name}, Avg Mark: {result.avg_mark:.2f}")

def select_3(subject_id: int):
    result = (
        session.query(
            Group.id,
            Group.name,
            func.avg(Mark.mark).label("avg_mark")
        )
        .join(Student, Group.id == Student.group_id)
        .join(Mark, Student.id == Mark.student_id)
        .filter(Mark.subject_id == subject_id)
        .group_by(Group.id, Group.name)
        .all()
    )
    for group in result:
        print(f"Group ID: {group.id}, Group Name: {group.name}, Avg Mark: {group.avg_mark:.2f}")

def select_4():
    result = session.query(func.avg(Mark.mark)).scalar()
    print(f"Average Mark: {result:.2f}")

def select_5(teacher_id: int):
    result = (
        session.query(Subject.id, Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )
    print(f"Courses by teacher {teacher_id}:")
    for course in result:
        print(f"ID: {course.id}, Name: {course.name}")

def select_6(group_id: int):
    result = (
        session.query(Student.id, Student.name, Student.email)
        .filter(Student.group_id == group_id)
        .all()
    )
    print(f"Students in group {group_id}:")
    for student in result:
        print(f"ID: {student.id}, Name: {student.name}, Email: {student.email}")

def select_7(group_id: int, subject_id: int):
    result = (
        session.query(Student.id, Student.name, Mark.mark)
        .join(Mark, Student.id == Mark.student_id)
        .filter(Student.group_id == group_id, Mark.subject_id == subject_id)
        .all()
    )
    print(f"Marks for group {group_id} in subject {subject_id}:")
    for student in result:
        print(f"Student ID: {student.id}, Name: {student.name}, Mark: {student.mark}")

def select_8(teacher_id: int):
    result = (
        session.query(func.avg(Mark.mark))
        .join(Subject, Mark.subject_id == Subject.id)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )
    print(f"Average mark by teacher {teacher_id}: {result:.2f}")

def select_9(student_id: int):
    result = (
        session.query(Subject.id, Subject.name)
        .join(Mark, Subject.id == Mark.subject_id)
        .filter(Mark.student_id == student_id)
        .distinct()
        .all()
    )
    print(f"Courses attended by student {student_id}:")
    for course in result:
        print(f"ID: {course.id}, Name: {course.name}")

def select_10(student_id: int, teacher_id: int):
    result = (
        session.query(Subject.id, Subject.name)
        .join(Mark, Subject.id == Mark.subject_id)
        .filter(Mark.student_id == student_id, Subject.teacher_id == teacher_id)
        .distinct()
        .all()
    )
    print(f"Courses taught by teacher {teacher_id} to student {student_id}:")
    for course in result:
        print(f"ID: {course.id}, Name: {course.name}")

if __name__ == "__main__":
    select_1()
    select_2(2)
    select_3(5)
    select_4()
    select_5(1)
    select_6(2)
    select_7(3, 3)
    select_8(4)
    select_9(35)
    select_10(17, 5)