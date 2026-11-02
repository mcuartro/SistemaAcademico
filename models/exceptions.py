class DuplicateStudentException(Exception):
    #Se lanza cuando el estudiante ya está matriculado en el grupo.
    def __init__(self, codigo_estudiantil, id_grupo):
        super().__init__(f"Error de matrícula: El estudiante con código {codigo_estudiantil} ya se encuentra matriculado en el grupo {id_grupo}.")


class MaxCapacityReachedException(Exception):
    #Se lanza cuando el grupo alcanzó la capacidad máxima.
    def __init__(self, id_grupo, capacidad):
        super().__init__(f"Error de cupo: El grupo {id_grupo} ya alcanzó su capacidad máxima de {capacidad} estudiantes.")


class StudentNotEnrolledException(Exception):
    #Se lanza cuando el estudiante que se desea retirar no está matriculado."
    def __init__(self, codigo_estudiantil, id_grupo):
        super().__init__(f"Error de retiro: El estudiante con código {codigo_estudiantil} no está matriculado en el grupo {id_grupo}.")


class CourseNotFoundException(Exception):
    #Se lanza cuando la asignatura buscada no existe.
    def __init__(self, id_course):
        super().__init__(f"Error de búsqueda: La asignatura con código {id_course} no existe en el sistema.")


class ProgramNotFoundException(Exception):
    #Se lanza cuando el programa académico buscado no existe.
    def __init__(self, id_program):
        super().__init__(f"Error de búsqueda: El programa académico con código {id_program} no existe en el sistema.")