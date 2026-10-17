from models.course import Course

class CourseController:

    def __init__(self):
        self.courses = []

    def add_course(self, idCourse, name, credit, program):
        course = Course(idCourse, name, credit, program)
        self.courses.append(course)

    def get_courses(self):
        return self.courses.copy()