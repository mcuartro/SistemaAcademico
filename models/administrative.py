from models.user import User

class Administrative(User):

    def __init__(self, idDocument, name, email, idEmployee, dependency, position, workday):
        super().__init__(idDocument, name, email)
        self.set_idEmployee(idEmployee)
        self.set_dependency(dependency)
        self.set_position(position)
        self.set_workday(workday)

    def get_idEmployee(self):
        return self._idEmployee 

    def set_idEmployee(self, idEmployee):
        if(idEmployee > 0):
            self._idEmployee = idEmployee
        else:
            raise ValueError("El numero de empleado no puede ser 0")

    def get_dependency(self):
        return self._dependency 

    def set_dependency(self, dependency):
        if(dependency != ""):
            self._dependency = dependency
        else:
            raise ValueError("La dependencia no puede estar vacía")

    def get_position(self):
        return self._position 

    def set_position(self, position):
        if(position != ""):
            self._position + position
        else:
            raise ValueError("El cargo no puede estar vacío")

    def get_workday(self):
        return self._workday 

    def set_workday(self, worday):
        if(worday != ""):
            self._workday = worday
        else:
            raise ValueError("La jornada no puede estar vacía")

    def show_info(self):
        return f"{super().show_info()} - Numero de empleado: {self.get_idEmployee()} - Dependencia: {self.get_dependency()} - Cargo: {self.get_position()} - Jornada: {self.get_workday()}"