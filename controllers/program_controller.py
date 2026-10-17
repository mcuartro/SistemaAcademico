from models.program import Program
class ProgramController:

    def __init__(self):
        self.programs = []

    def add_program(self, idProgram, name, faculty, semesters):
        program = Program(idProgram, name, faculty, semesters)
        self.programs.append(program)

    def get_programs(self):
        return self.programs.copy()