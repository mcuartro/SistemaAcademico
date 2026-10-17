from models.user import User

class Student(User):

    def __init__(self, idDocument, name, email, idStudent, program, semester, average):
        super().__init__(idDocument, name, email)
        self.set_idStudent(idStudent)
        self.set_program(program)
        self.set_semester(semester)
        self.set_average(average)

    def get_idStudent(self):
        return self._idStudent 

    def set_idStudent(self, idStudent):
        if(idStudent > 0):
            self._idStudent = idStudent
        else:
            raise ValueError("El codigo de estudiante no puede ser 0")

    def get_program(self):
        return self._program 

    def set_program(self, program):
        if(program != ""):
            self._program = program
        else:
            raise ValueError("El programa no puede estar vacio")

    def get_semester(self):
        return self._semester

    def set_semester(self, semester):
        if(semester > 0):
            self._semester = semester
        else:
            raise ValueError("El semestre tiene que ser mayor que 0")

    def get_average(self):
        return self._average

    def set_average(self, average):
        if(0 < average < 5):
            self._average = average
        else:
            raise ValueError("El promedio acumulado tiene que ser mayor a 0 y menor a 5")

    def show_info(self):
        return f"{super().show_info()} - Codigo estudiante: {self.get_idStudent()} - Programa: {self.get_program()} - Semestre: {self.get_semester()} - Promedio acumulado: {self.get_average()}"

    def primary_activity(self):
        return f"El estudiante {self.name} esta estudiando en el programa {self.get_program()} y se encuentra en el semestre {self.get_semester()}"