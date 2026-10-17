class Course:

    def __init__(self, idCourse, name, credit, program):
        self.set_idCourse(idCourse)
        self.set_name(name)
        self.set_credit(credit)
        self.set_program(program)

    def get_idCourse(self):
        return self._idCourse

    def set_idCourse(self, idCourse):
        if(idCourse > 0):
            self._idCourse = idCourse
        else:
            raise ValueError("El codigo del curso debe ser mayor a 0")

    def get_name(self):
        return self._name

    def set_name(self, name):
        if(name != ""):
            self._name = name
        else:
            raise ValueError("El nombre del curso no puede estar vacío")

    def get_credit(self):
        return self._credit

    def set_credit(self, credit):
        if(credit > 0):
            self._credit = credit
        else:
            raise ValueError("Los creditos del curso tiene que ser mayor a 0")

    def get_program(self):
        return self._program 

    def set_program(self, program):
        if(program != ""):
            self._program = program
        else:
            raise ValueError("El programa academico no puede estar vacío")

    def show_info(self):
        return f"Codigo curso: {self.get_idCourse()} - Nombre: {self.get_name()} - Creditos: {self.get_credit()} - Programa academico: {self.get_program()}"