#declaracion de variable
nombreEmpleado="pedro"
print(nombreEmpleado)
edadEmpledado=40
print(edadEmpledado)
sueldoEmpleado=5000.89
print(sueldoEmpleado)
booleano="true"
print (booleano)

#entrada de datos por medio del teclado
edadEstudiante=str(input("Introduce su edad del Estudiante:"))
print("la edad del estudiante es:",edadEstudiante)

nombreEstudiante=str(input("Introduce el nombre del Estudiante:"))
print("el nombre del estudiante es:",nombreEstudiante)

calificacionEstudiante=float(input("intrudce la calificacion del estudiante" ))
print("la calificacion del estudaiante es:", calificacionEstudiante)

numero1=2
numero2=3
numero3=1
suma=numero1+numero2+numero3
print("la suma es: ",suma)

baseRectangulo=float(input("Introduzca la base del rectangulo: "))
alturaRectangulo=float(input("Introduzca la altura del rectangulo: "))
areaRectangulo=baseRectangulo*alturaRectangulo
print("el resultado del area dek rectangulo es: ", areaRectangulo)

#8.- sentencia if else

calificacionProgramacion=float(input("introduce la calificacion de programacion"))
calificacionRedes=float(input("introduce la calificacion de Redes"))
calificacionMatematicas=float(input("introduce la calificacion de matematicas"))
promedioCalificaciones=(calificacionProgramacion+calificacionRedes+calificacionMatematicas)/3
if promedioCalificaciones>=70:
    print("Aprobado", promedioCalificaciones)
else:
    print("Debes estudiar mas,Estas reprobado",promedioCalificaciones)