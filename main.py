from controllers.course_controller import CourseController
from controllers.program_controller import ProgramController
from controllers.user_controller import UserController

def show_programs(program_controller):
    programs = program_controller.get_programs()

    if not programs:
        print("\n No hay programas registrados")
        return

    for program in programs:
        print(f"\n {program.show_info()}")
        print(program.primary_activity())

def show_courses(course_controller):
    courses = course_controller.get_courses()

    if not courses:
        print("\n No hay cursos registrados")

    for course in courses:
        print(f"\n {course.show_info()}")
        print(course.primary_activity())

def show_users(user_controller):
    users = user_controller.get_users()

    if not users:
        print("\n No hay usuarios")

    for user in users:
        print(f"\n {user.show_info()}")
        print(user.primary_activity())

def main():
    course_controller = CourseController()
    program_controller = ProgramController()
    user_controller = UserController()
    
    idDocument = 1004187
    name = "John Doe"
    email = "johndoe@example.com"
    idStudent = 12345
    program = "Ingeniería de Software"
    semester = 5
    average = 3.5
    user_controller.add_student(idDocument, name, email, idStudent, program, semester, average)

    idDocument = 1089767
    name = "Jane Smith"
    email = "janesmith@example.com"
    idStudent = 19786
    program = "Ingeniería Electrónica"
    semester = 7
    average = 4.5
    user_controller.add_student(idDocument, name, email, idStudent, program, semester, average)

    idDocument = 178546
    name = "Maria Gonzalez"
    email = "mariagonzalez@university.com"
    idEmployee = 87865
    faculty = "Ingeniería"
    employmentType = "Tiempo completo"
    hoursWeek = 20
    user_controller.add_teacher(idDocument, name, email, idEmployee, faculty, employmentType, hoursWeek)

    idDocument = 198734
    name = "Oscar Ramirez"
    email = "oscarramirez@university.com"
    idEmployee = 87645
    faculty = "Ciencias"
    employmentType = "Medio tiempo"
    hoursWeek = 15
    user_controller.add_teacher(idDocument, name, email, idEmployee, faculty, employmentType, hoursWeek)

    idDocument = 1875459
    name = "Carlos Mendoza"
    email = "carlosmendoza@university.com"
    idEmployee = 873435
    dependency = "Administración"
    position = "Coordinador Académico"
    workday = "Jornada Completa"
    user_controller.add_administrative(idDocument, name, email, idEmployee, dependency, position, workday)

    idDocument = 1987234
    name = "Luis espinoza"
    email = "luisespinoza@university.com"
    idEmployee = 67845
    dependency = "Finanzas"
    position = "Contador"
    workday = "Jornada Parcial"
    user_controller.add_administrative(idDocument, name, email, idEmployee, dependency, position, workday)

    while True:
        print("\n Menú")
        print("1. Agregar programa academico")
        print("2. Agregar curso")
        print("3. Agregar estudiante")
        print("4. Agregar maestro")
        print("5. Agregar administrativo")
        print("6. Mostrar programas academicos")
        print("7. Mostrar cursos")
        print("8. Mostrar usuarios")
        print("0. Salir")

        option = input("Seleccione una opción: ")

        match option:
            case "1":
                idProgram = int(input("Ingrese el numero del programa a crear: "))
                name = input("Ingrese el nombre del programa a crear: ")
                faculty = input("Ingrese la facultad del programa a crear: ")
                semesters = int(input("Ingrese la cantidad de semestres del programa a crear: "))

                program_controller.add_program(idProgram, name, faculty, semesters)
                print("\n Producto agregado con éxito")

            case "2":
                idCourse = int(input("Ingrese el codigo del curso a crear: "))
                name = input("Ingrese el nombre del curso a crear: ")
                credit = int(input("Ingrese el costo en creditos del curos a crear: "))
                program = input("Ingrese el programa al que pertenece el curso a crear: ")

                course_controller.add_course(idCourse, name, credit, program)
                print("\n Curso agregado con éxito")

            case "3":
                idDocument = int(input("Ingrese el numero de documento del estudiante a añadir: "))
                name = input("Ingrese el nombre del estudiante a añadir: ")
                email = input("Ingrese el correo del estudiante a añadir: ")
                idStudent = int(input("Ingrese el codigo de estudiante del estudiante a añadir: "))
                program = input("Ingrese el programa al que pertenece el estudiante a añadir: ")
                semester = int(input("Ingrese el numero de semestres cursados del estudiante a añadir: "))
                average = float(input("Ingrese el promedio acumulado del estudiante a añadir: "))

                user_controller.add_student(idDocument, name, email, idStudent, program, semester, average)
                print("\n Estudiante añadido con éxito")

            case "4":
                idDocument = int(input("Ingrese el numero de documento del maestro a añadir: "))
                name = input("Ingrese el nombre del maestro a añadir: ")
                email = input("Ingrese el correo del maestro a añadir: ")
                idEmployee = int(input("Ingrese el codigo de empleado del maestro a añadir: "))
                faculty = input("Ingrese la facultad en la que enseña el maestro a añadir: ")
                employmentType = input("Ingrese el tipo de contratacion que tiene el maestro a añadir: ")
                hoursWeek = int(input("Ingrese el numero de horas semanales lavoradas del maestro a añadir: "))

                user_controller.add_teacher(idDocument, name, email, idEmployee, faculty, employmentType, hoursWeek)
                print("\n Maestro añadido con éxito")

            case "5":
                idDocument = int(input("Ingrese el numero de documento del administrativo a añadir: "))
                name = input("Ingrese el nombre del administrativo a añadir: ")
                email = input("Ingrese el correo del administrativo a añadir: ")
                idEmployee = int(input("Ingrese el codigo de empleado del administrativo a añadir: "))
                dependency = input("Ingrese la dependencia del administrativo a añadir: ")
                position = input("Ingrese el cargo del administrativo a añadir: ")
                workday = input("ingrese la jornada del administrativo a añadir: ")

                user_controller.add_administrative(idDocument, name, email, idEmployee, dependency, position, workday)
                print("\n Administrativo añadido con éxito")

            case "6":
                show_programs(program_controller)

            case "7":
                show_courses(course_controller)

            case "8":
                show_users(user_controller)

            case "0":
                print("\nFinalizando programa")
                break
        
            case _:
                print("\n opción inválida")

if __name__ == "__main__":
    main()