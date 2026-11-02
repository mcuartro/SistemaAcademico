from models.program import Program
from models.exceptions import ProgramNotFoundException

class ProgramController:

    def __init__(self):
        self.programs = []

    def add_program(self, idProgram, name, faculty, semesters):
        program = Program(idProgram, name, faculty, semesters)
        self.programs.append(program)
        return program

    def get_programs(self):
        return self.programs.copy()

    def find_program(self, idProgram):
        for program in self.programs:
            if program.get_idProgram() == idProgram:
                return program
        raise ProgramNotFoundException(idProgram)