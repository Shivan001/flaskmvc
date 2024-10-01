from App.models import Student
from App.database import db

def create_student(name):
    new_student = Student(name=name)
    db.session.add(new_student)
    db.session.commit()
    return new_student

def get_all_students():
    return Student.query.all()

def get_student_by_id(student_id):
    return Student.query.get(student_id)
