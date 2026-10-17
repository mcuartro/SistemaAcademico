Integrante: 
    Miguel Angel Cuartas Rojas
Descripcion general del sistema:
    El sistema es un aplicativo de gestion academica pensado para una universidad, el cual permite crear Programas, Cursos y Usuarios. A su vez puede mostrar la informacion necesaria de cada clase de forma eficaz.
Estructura de lso archivos:
   Los archivos estan estructurados en un archivo principal en el cual se ejecuta el programa, una carpeta models en la cual se crearon todas la clases necesarias del programay una carpeta controllers en la que se hizo el intermediario entre el archivo principal y las clases, a su vez tambien manejan la lista de los objetos de cada clase.
Instrucciones para ejecutar el proyecto:
   Para ejecutar el projecto hay que abrir el archivo main.py desde la terminal o consola, una vez se ejecuta el archivo la consola muestra un menu en el cual se puede navegar para crear programas, cursos y usuarios o por el contrario mostrar los que ya tenga almacenados en memoria.
Explicacion herencia, sobre escritura y el polimorfismo:
   La herencia la aplique en la clase user y sus "hijas" (estudiante, administrativo y profesor) en un principio pense pasar el atributo idEmployee a la clase User por lo que se compartia en las clases administrativo y profesor, pero me generaba la duda ya que en la clase estudiante es diferente (idStudent), en si el atributo es el mismo pero cambia el nombre, por eso preferi dejarlo como algo individual de cada clase.
   El polimorfismo se logra de forma sencilla al crear el metodo en cada clase con sus caracteristicas de esa clase, asi al llamar al metodo con su respectiva clase padre sabran exactamente que codigo ejecutar.
Hice uso de la IA para ayudarme a solucionar un problema con el if __name__ == "__main__": main() al final del archivo main.py. Ya que a la hora de probar el programa para testearlo este no me estaba funcionando y no entendia porque, la IA me ayudo a ver que el problema era que el if estaba estructurado dentro del case_: y por eso el programa no lo ejecutaba, luego de sacarlo del todo el programa me funciono y pude ver algunos errores de sintaxis que con el codigo de error pude solucionar sin problema.
