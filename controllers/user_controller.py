from models.student import Student
from models.teacher import Teacher
from models.administrative import Administrative

class UserController:

    def __init__(self):
        self.users = []

    def add_student(self, idDocument, name, email, idStudent, program, semester, average):
        student = Student(idDocument, name, email, idStudent, program, semester, average)
        self.users.append(student)

    def add_teacher(self, idDocument, name, email, idEmployee, faculty, employmentType, hoursWeek):
        teacher = Teacher(idDocument, name, email, idEmployee, faculty, employmentType, hoursWeek)
        self.users.append(teacher)

    def add_administrative(self, idDocument, name, email, idEmployee, dependency, position, workday):
        administrative = Administrative(idDocument, name, email, idEmployee, dependency, position, workday)
        self.users.append(administrative)

    def get_users(self):
        return self.users.copy()