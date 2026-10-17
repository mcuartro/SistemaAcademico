from models.user import User

class Teacher(User):

    def __init__(self, idDocument, name, email, idEmployee, faculty, employmentType, hoursWeek):
        super().__init__(idDocument, name, email)
        self.set_idEmployee(idEmployee)
        self.set_faculty(faculty)
        self.set_employmentType(employmentType)
        self.set_hoursWeek(hoursWeek)

    def get_idEmployee(self):
        return self._idEmployee 

    def set_idEmployee(self, idEmployee):
        if(idEmployee > 0):
            self._idEmployee = idEmployee
        else:
            raise ValueError("El numero de empleado no puede ser 0")

    def get_faculty(self):
        return self._faculty

    def set_faculty(self, faculty):
        if(faculty != ""):
            self._faculty = faculty
        else:
            raise ValueError("La facultad no puede estar vacía")

    def get_employmentType(self):
        return self._employmentType 

    def set_employmentType(self, employmentType):
        if(employmentType != ""):
            self._employmentType = employmentType
        else:
            raise ValueError("El tipo de contratación no puede estar vacío")

    def get_hoursWeek(self):
        return self._hoursWeek 

    def set_hoursWeek(self, hoursWeek):
        if(hoursWeek > 0 ):
            self._hoursWeek = hoursWeek
        else:
            raise ValueError("La cantidad de horas semanales tiene que ser mayor a 0")

    def show_info(self):
        return f"{super().show_info()} - Numero de empleado: {self.get_idEmployee()} - Facultad: {self.get_faculty()} - Tipo de contratación: {self.get_employmentType()} - Horas semanales: {self.get_hoursWeek()}"

    def primary_activity(self):
        return f"El maestro {self.name} esta enseñando en la facultad {self.get_faculty()}"