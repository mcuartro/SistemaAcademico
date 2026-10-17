class Program:

    def __init__(self, idProgram, name, faculty, semesters):
        self.set_idProgram(idProgram)
        self.set_name(name)
        self.set_faculty(faculty)
        self.set_semesters(semesters)

    def get_idProgram(self):
        return self._idProgram

    def set_idProgram(self, idProgram):
        if(idProgram > 0):
            self._idProgram = idProgram
        else:
            raise ValueError("El codigo del programa no puede ser 0")

    def get_name(self):
        return self._name

    def set_name(self, name):
        if(name != ""):
            self._name = name
        else:
            raise ValueError("El nombre del programa no puede estar vacío")

    def get_faculty(self):
        return self._faculty

    def set_faculty(self, faculty):
        if(faculty != ""):
            self._faculty = faculty
        else:
            raise ValueError("La facultad no puede estar vacía")

    def get_semesters(self):
        return self._semesters

    def set_semesters(self, semesters):
        if(semesters > 0):
            self._semesters = semesters
        else:
            raise ValueError("La cantidad de semestres tiene que ser mayor que 0")

    def show_info(self):
        return f"Codigo programa: {self.get_idProgram()} - Nombre: {self.get_name()} - Facultad: {self.get_faculty()} - Semestres: {self.get_semesters()}"