from models.course import Course
from models.teacher import Teacher
from models.student import Student
from models.schedule import Schedule
from models.exceptions import (
    DuplicateStudentException,
    MaxCapacityReachedException,
    StudentNotEnrolledException
)

class Group:
    def __init__(self, idGroup, course, teacher, maxCapacity, schedule):
        self.set_idGroup(idGroup)
        self.set_course(course)
        self.set_teacher(teacher)
        self.set_maxCapacity(maxCapacity)
        self.set_schedule(schedule)
        self._students = []

    def get_idGroup(self):
        return self._idGroup

    def set_idGroup(self, idGroup):
        if idGroup <= 0:
            self._idGroup = idGroup
        else:
            raise ValueError("El código del grupo debe ser mayor a 0")

    def get_course(self):
        return self._course

    def set_course(self, course):
        if isinstance(course, Course):
            self._course = course
        else:
            raise ValueError("Se debe asignar un curso válido")

    def get_teacher(self):
        return self._teacher
        
    def set_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self._teacher = teacher
        else:
            raise ValueError("Se debe asignar un profesor válido")

    def get_maxCapacity(self):
        return self._maxCapacity

    def set_maxCapacity(self, maxCapacity):
        if maxCapacity > 0:
            self._maxCapacity = maxCapacity
        else:
            raise ValueError("La capacidad máxima debe ser mayor a 0")

    def get_schedule(self):
        return self._schedule

    def set_schedule(self, schedule):
        if isinstance(schedule, Schedule):
            self._schedule = schedule
        else:
            raise ValueError("El horario debe ser una un objeto valido de la lista de horarios")
        
    def get_students(self):
        return self._students.copy()

    def mostrar_informacion_grupo(self):
        return (
            f"Grupo: {self.get_idGroup()} | Capacidad: {len(self._students)}/{self.get_maxCapacity()}\n"
            f"Asignatura: {self._course.get_name()} (Código: {self._course.get_idCourse()})\n"
            f"Docente: {self._teacher.name} (ID Empleado: {self._teacher.get_idEmployee()})\n"
            f"Horario: {self._schedule.show_info()}"
        )

    def matricular_estudiante(self, estudiante):
        if not isinstance(estudiante, Student):
            raise ValueError("Solo se pueden matricular estudiantes existentes")
        
        # Verificar si el estudiante ya está matriculado
        for s in self._students:
            if s.get_idStudent() == estudiante.get_idStudent():
                raise DuplicateStudentException(estudiante.get_idStudent(), self._idGroup)

        # Verificar si se ha alcanzado la capacidad máxima del grupo
        if len(self._students) >= self._maxCapacity:
            raise MaxCapacityReachedException(self._idGroup, self._maxCapacity)

        self._students.append(estudiante)

    def retirar_estudiante(self, codigo_estudiantil):
        for s in self._students:
            if s.get_idStudent() == codigo_estudiantil:
                self._students.remove(s)
                return
        # Si no se encuentra el estudiante se lanza una excepción
        raise StudentNotEnrolledException(codigo_estudiantil, self._idGroup)

    def mostrar_estudiantes(self):
        if not self._students:
            return "No hay estudiantes matriculados en este grupo."
        listado = f"Estudiantes matriculados en el grupo {self.get_idGroup()}:\n"
        for s in self._students:
            listado += f"  - {s.show_info()}\n"
        return listado.strip()