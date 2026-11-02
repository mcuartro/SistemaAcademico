from models.course import Course
from models.exceptions import CourseNotFoundException

class CourseController:

    def __init__(self):
        self.courses = []

    def add_course(self, idCourse, name, credit, program):
        course = Course(idCourse, name, credit, program)
        self.courses.append(course)

    def get_courses(self):
        return self.courses.copy()

    def find_course(self, idCourse):
        for course in self.courses:
            if course.get_idCourse() == idCourse:
                return course
        raise CourseNotFoundException(idCourse)