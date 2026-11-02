from controllers.course_controller import CourseController
from controllers.program_controller import ProgramController
from controllers.user_controller import UserController
from controllers.group_controller import GroupController
from models.user import User
from models.schedule import Schedule
from models.exceptions import (
    DuplicateStudentException,
    MaxCapacityReachedException,
    StudentNotEnrolledException,
    CourseNotFoundException,
    ProgramNotFoundException
)

# Se declaran las funciones para mostrar los programas, cursos y usuarios
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

def show_groups(group_controller):
    groups = group_controller.get_groups()
    if not groups:
        print("\n No hay grupos académicos registrados")
        return
    for group in groups:
        print(f"\n{group.mostrar_informacion_grupo()}")
        print(group.mostrar_estudiantes())

# se ejecuta para hacer pruebas
def test(program_controller, course_controller, user_controller, group_controller):
    print("\n--- Pruebas ---")

    # test crear un usuario tipo User
    print("\n Prueba 1. Intento de instanciar directamente la clase abstracta User:")
    try:
        usuario_invalido = User(12345, "Miguel test", "miguel@test.com")
    except TypeError as e:
        print(f"\n Error al crear usuario: {e}")

    # test creación de programas, asignaturas, docentes, estudiantes y horarios
    print("\n Prueba 2. Creación de programas, asignaturas, docentes, estudiantes y horarios:")
    program_controller.add_program(1, "Ingeniería de Software", "Ingeniería", 10)
    program_controller.add_program(2, "Ingeniería Electrónica", "Ingeniería", 10)

    curso_poo = course_controller.add_course(101, "Programación Orientada a Objetos", 4, "Ingeniería de Software")
    curso_bd = course_controller.add_course(102, "Bases de Datos", 3, "Ingeniería de Software")

    user_controller.add_student(1004187, "John Doe", "johndoe@test.com", 12345, "Ingeniería de Software", 5, 3.5)
    user_controller.add_student(1089767, "Jane Smith", "janesmith@test.com", 19786, "Ingeniería Electrónica", 7, 4.5)
    user_controller.add_student(1099888, "Ana Torres", "anatorres@test.com", 54321, "Ingeniería de Software", 3, 4.2)

    user_controller.add_teacher(178546, "Maria Gonzalez", "mariagonzalez@test.com", 87865, "Ingeniería", "Tiempo completo", 20)
    user_controller.add_teacher(198734, "Oscar Ramirez", "oscarramirez@test.com", 87645, "Ciencias", "Medio tiempo", 15)

    user_controller.add_administrative(1875459, "Carlos Mendoza", "carlosmendoza@test.com", 873435, "Administración", "Coordinador Académico", "Jornada Completa")
    user_controller.add_administrative(1987234, "Luis Espinoza", "luisespinoza@test.com", 67845, "Finanzas", "Contador", "Jornada Parcial")

    horario_1 = Schedule("Lunes y Miércoles", "08:00", "10:00", "Salón B-201")
    horario_2 = Schedule("Martes y Jueves", "14:00", "16:00", "Laboratorio C-105")
    print("  -> Entidades base y objetos de horario creados correctamente.")

    # test creación de al menos dos grupos académicos
    print("\n Prueba 3. Creación de dos grupos académicos:")
    docente_1 = user_controller.find_teacher(87865)
    docente_2 = user_controller.find_teacher(87645)

    grupo_1 = group_controller.add_group(1, curso_poo, docente_1, 2, horario_1)
    grupo_2 = group_controller.add_group(2, curso_bd, docente_2, 3, horario_2)
    print(grupo_1.mostrar_informacion_grupo())
    print(grupo_2.mostrar_informacion_grupo())

    # test matrícula correcta de estudiantes
    print("\n Prueba 4. Matrícula correcta de estudiantes en el Grupo 1:")
    est_john = user_controller.find_student(12345)
    est_jane = user_controller.find_student(19786)
    est_ana = user_controller.find_student(54321)

    try:
        grupo_1.matricular_estudiante(est_john)
        grupo_1.matricular_estudiante(est_jane)
        print("  -> Estudiantes John Doe y Jane Smith matriculados con éxito.")
        print(grupo_1.mostrar_estudiantes())
    except Exception as e:
        print(f"  -> Error inesperado: {e}")

    # test intento de matricular un estudiante duplicado
    print("\n Prueba 5. Intento de matricular un estudiante duplicado (John Doe):")
    try:
        grupo_1.matricular_estudiante(est_john)
    except DuplicateStudentException as e:
        print(f"  -> [Excepción Controlada] {e}")

    # test intento de superar la capacidad de un grupo
    print("\n Prueba 6. Intento de superar la capacidad máxima del Grupo 1 (Cupo: 2):")
    try:
        grupo_1.matricular_estudiante(est_ana)
    except MaxCapacityReachedException as e:
        print(f"  -> [Excepción Controlada] {e}")

    # test retiro correcto de un estudiante
    print("\n Prueba 7. Retiro correcto de un estudiante (Jane Smith - Código 19786):")
    try:
        grupo_1.retirar_estudiante(19786)
        print("  -> Estudiante retirado exitosamente.")
        print(grupo_1.mostrar_estudiantes())
    except StudentNotEnrolledException as e:
        print(f"  -> Error inesperado: {e}")

    # test intento de retirar un estudiante inexistente en el grupo
    print("\n Prueba 8. Intento de retirar un estudiante no matriculado (Código 99999):")
    try:
        grupo_1.retirar_estudiante(99999)
    except StudentNotEnrolledException as e:
        print(f"  -> [Excepción Controlada] {e}")

    # test búsqueda de una asignatura inexistente
    print("\n Prueba 9. Búsqueda de una asignatura inexistente (Código 999):")
    try:
        course_controller.find_course(999)
    except CourseNotFoundException as e:
        print(f"  -> [Excepción Controlada] {e}")

    # test búsqueda de un programa académico inexistente
    print("\n Prueba 10. Búsqueda de un programa académico inexistente (Código 888):")
    try:
        program_controller.find_program(888)
    except ProgramNotFoundException as e:
        print(f"  -> [Excepción Controlada] {e}")

    # test continuidad del programa
    print("\n Prueba 11. Continuidad del sistema tras el manejo de excepciones:")
    print("==========================================================\n")


    # añadado submenús para la gestión de usuarios, programas y cursos, y grupos y matrículas
def menu_usuarios(user_controller):
    while True:
        print("\n--- Submenú: Gestión de Usuarios ---")
        print("1. Agregar estudiante")
        print("2. Agregar docente")
        print("3. Agregar administrativo")
        print("4. Mostrar usuarios y su actividad principal")
        print("0. Volver al menú principal")

        option = input("Seleccione una opción: ")

        try:
            match option:
                case "1":
                    idDocument = int(input("Documento del estudiante: "))
                    name = input("Nombre del estudiante: ")
                    email = input("Correo del estudiante: ")
                    idStudent = int(input("Código estudiantil: "))
                    program = input("Programa al que pertenece: ")
                    semester = int(input("Semestre actual: "))
                    average = float(input("Promedio acumulado: "))
                    user_controller.add_student(idDocument, name, email, idStudent, program, semester, average)
                    print("\nEstudiante añadido con éxito")

                case "2":
                    idDocument = int(input("Documento del docente: "))
                    name = input("Nombre del docente: ")
                    email = input("Correo del docente: ")
                    idEmployee = int(input("Código de empleado: "))
                    faculty = input("Facultad: ")
                    employmentType = input("Tipo de contratación: ")
                    hoursWeek = int(input("Horas semanales laboradas: "))
                    user_controller.add_teacher(idDocument, name, email, idEmployee, faculty, employmentType, hoursWeek)
                    print("\nDocente añadido con éxito")

                case "3":
                    idDocument = int(input("Documento del administrativo: "))
                    name = input("Nombre del administrativo: ")
                    email = input("Correo del administrativo: ")
                    idEmployee = int(input("Código de empleado: "))
                    dependency = input("Dependencia: ")
                    position = input("Cargo: ")
                    workday = input("Jornada: ")
                    user_controller.add_administrative(idDocument, name, email, idEmployee, dependency, position, workday)
                    print("\nAdministrativo añadido con éxito")

                case "4":
                    show_users(user_controller)

                case "0":
                    break

                case _:
                    print("\nOpción inválida")

        except ValueError as e:
            print(f"\n[Error de validación] {e}")


def menu_programas_y_cursos(program_controller, course_controller):
    while True:
        print("\n--- Submenú: Programas y Asignaturas ---")
        print("1. Agregar programa académico")
        print("2. Buscar programa por código")
        print("3. Mostrar programas académicos")
        print("4. Agregar asignatura (curso)")
        print("5. Buscar asignatura por código")
        print("6. Mostrar asignaturas")
        print("0. Volver al menú principal")

        option = input("Seleccione una opción: ")

        try:
            match option:
                case "1":
                    idProgram = int(input("Ingrese el código del programa a crear: "))
                    name = input("Ingrese el nombre del programa a crear: ")
                    faculty = input("Ingrese la facultad del programa a crear: ")
                    semesters = int(input("Ingrese la cantidad de semestres: "))
                    program_controller.add_program(idProgram, name, faculty, semesters)
                    print("\nPrograma agregado con éxito")

                case "2":
                    idProgram = int(input("Ingrese el código del programa a buscar: "))
                    program = program_controller.find_program(idProgram)
                    print(f"\nPrograma encontrado: {program.show_info()}")

                case "3":
                    show_programs(program_controller)

                case "4":
                    idCourse = int(input("Ingrese el código del curso a crear: "))
                    name = input("Ingrese el nombre del curso a crear: ")
                    credit = int(input("Ingrese los créditos del curso: "))
                    program = input("Ingrese el programa al que pertenece el curso: ")
                    course_controller.add_course(idCourse, name, credit, program)
                    print("\nCurso agregado con éxito")

                case "5":
                    idCourse = int(input("Ingrese el código de la asignatura a buscar: "))
                    course = course_controller.find_course(idCourse)
                    print(f"\nAsignatura encontrada: {course.show_info()}")

                case "6":
                    show_courses(course_controller)

                case "0":
                    break

                case _:
                    print("\nOpción inválida")

        except (ProgramNotFoundException, CourseNotFoundException, ValueError) as e:
            print(f"\n[Operación no completada] {e}")


def menu_grupos(group_controller, course_controller, user_controller):
    while True:
        print("\n--- Submenú: Grupos Académicos y Matrículas ---")
        print("1. Crear grupo académico")
        print("2. Matricular estudiante en grupo")
        print("3. Retirar estudiante de grupo")
        print("4. Mostrar grupos académicos y matriculados")
        print("0. Volver al menú principal")

        option = input("Seleccione una opción: ")

        try:
            match option:
                case "1":
                    idGroup = int(input("Código del grupo académico: "))
                    idCourse = int(input("Código de la asignatura existente: "))
                    idTeacher = int(input("Código de empleado del docente responsable: "))
                    maxCapacity = int(input("Capacidad máxima del grupo: "))
                    day = input("Día(s) de clase: ")
                    startTime = input("Hora de inicio (ej. 08:00): ")
                    endTime = input("Hora de finalización (ej. 10:00): ")
                    classroom = input("Salón: ")

                    course = course_controller.find_course(idCourse)
                    teacher = user_controller.find_teacher(idTeacher)
                    if teacher is None:
                        print("\nError: No se encontró un docente con ese código de empleado.")
                    else:
                        schedule = Schedule(day, startTime, endTime, classroom)
                        group_controller.add_group(idGroup, course, teacher, maxCapacity, schedule)
                        print("\nGrupo académico creado con éxito")

                case "2":
                    idGroup = int(input("Código del grupo: "))
                    idStudent = int(input("Código estudiantil del alumno a matricular: "))
                    group = group_controller.find_group(idGroup)
                    student = user_controller.find_student(idStudent)

                    if group is None:
                        print("\nError: El grupo indicado no existe.")
                    elif student is None:
                        print("\nError: No existe un estudiante con ese código.")
                    else:
                        group.matricular_estudiante(student)
                        print("\nEstudiante matriculado con éxito")

                case "3":
                    idGroup = int(input("Código del grupo: "))
                    idStudent = int(input("Código estudiantil del alumno a retirar: "))
                    group = group_controller.find_group(idGroup)
                    if group is None:
                        print("\nError: El grupo indicado no existe.")
                    else:
                        group.retirar_estudiante(idStudent)
                        print("\nEstudiante retirado del grupo con éxito")

                case "4":
                    show_groups(group_controller)

                case "0":
                    break

                case _:
                    print("\nOpción inválida")

        except (
            CourseNotFoundException,
            DuplicateStudentException,
            MaxCapacityReachedException,
            StudentNotEnrolledException,
            ValueError
        ) as e:
            print(f"\n[Operación no completada] {e}")

# Se declara la funcion main que contiene el menu principal del programa
def main():
    course_controller = CourseController()
    program_controller = ProgramController()
    user_controller = UserController()
    group_controller = GroupController()

    test(
        program_controller,
        course_controller,
        user_controller,
        group_controller
    )

    # Se declara el menu principal del programa
    while True:
        print("\n=== MENÚ PRINCIPAL - SISTEMA ACADÉMICO ===")
        print("1. Gestión de Usuarios (Estudiantes, Docentes, Administrativos)")
        print("2. Gestión de Programas y Asignaturas")
        print("3. Gestión de Grupos Académicos y Matrículas")
        print("0. Salir")

        option = input("Seleccione un módulo: ")

        match option:
            case "1":
                menu_usuarios(user_controller)
            case "2":
                menu_programas_y_cursos(program_controller, course_controller)
            case "3":
                menu_grupos(group_controller, course_controller, user_controller)
            case "0":
                print("\nFinalizando programa")
                break
            case _:
                print("\nIngrese una opcion valida.")

if __name__ == "__main__":
    main()