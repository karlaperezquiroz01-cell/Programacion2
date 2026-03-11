#ACTIVIDAD 1
#declaracion de variables
nombreEmpleado="pedro"
print(nombreEmpleado)

edadEmpleado=40
print(edadEmpleado)

sueldoEmpleado=50000.89
print(sueldoEmpleado)

activo="true"
print(activo)

materias=["Programacion", "Bases de datos"]
print(materias)

#ACTIVIDAD 2
#entrada de datos por medio del teclado
nombreEstudiante=str(input("introduce el nombre del estudiante: "))
print("el nombre del estudiante es: ", nombreEstudiante)

edadEstudiante=int(input("introduce la edad del estudiante: "))
print("la edad del estudiante es:" , edadEstudiante)

calificacionEstudiante=float(input("introduce la calificacion del estudiante: "))
print("la calificacion del estudiante es: ", calificacionEstudiante)

#ACTIVIDAD 3
#suma de numeros
numero1=8
numero2=3
numero3=12
numero4=6
numero5=9
suma=numero1+numero2+numero3+numero4+numero5
print("La suma de los cinco numeros es: ", suma)

#ACTIVIDAD 4
#calcular area de figuras
baseRectangulo=float(input("Introduzca la base del rectangulo: "))
alturaRectangulo=float(input("Introduce la altura del rectangulo: "))
areaRectangulo=baseRectangulo*alturaRectangulo
print("El area del rectangulo es: ", areaRectangulo)

baseTriangulo=float(input("Introduce la base del triangulo: "))
alturaTriangulo=float(input("Introduce la altura del triangulo: "))
areaTriangulo=(baseTriangulo*alturaTriangulo)/2
print("El area del triangulo es: ", areaTriangulo)

#ACTIVIDAD 5
n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))
n4 = float(input("Numero 4: "))

resultado = n1 * n2 * n3 * n4

print("Resultado:", resultado)

#ACTIVIDAD 6
dias = int(input("Dias trabajados: "))
salario = float(input("Salario diario: "))

sueldo = dias * salario

print("Sueldo total:", sueldo)

#ACTIVIDAD 7
dolares = float(input("Cantidad en dolares: "))
euros = float(input("Cantidad en euros: "))

valor_dolar = 17
valor_euro = 18

pesos_dolares = dolares * valor_dolar
pesos_euros = euros * valor_euro

print("Dolares en pesos:", pesos_dolares)
print("Euros en pesos:", pesos_euros)

#ACTIVIDAD 8
#SENTENCIA IF ELSE
calificacionProgramacion=float(input("Introduce la calificacion de programacion: "))
calificacionRedes=float(input("Introduce la calificacion de redes: "))
calificacionMatematicas=float(input("Introduce la calificaion de matematicas: "))
promedioCalificaciones=(calificacionProgramacion+calificacionRedes+calificacionMatematicas)/3

if promedioCalificaciones>=70:
    print("Aprobado",promedioCalificaciones)
else:
    print("Debes estudiar más, estas reprobado",promedioCalificaciones)

#ACTIVADAD 9
numero=float(input("Introduce un numero: "))

if numero>=0:
    print("Numero positivo")
else:
    print("Numero negativo")

#ACTIVIDAD 10
edad = int(input("Edad: "))

if edad >= 18:
    print("Mayor de edad")

if edad < 18:
    print("Menor de edad")

#ACTIVIDAD 11
mes = int(input("Numero de mes (1-12): "))

if mes == 1:
    print("Enero")
if mes == 2:
    print("Febrero")
if mes == 3:
    print("Marzo")
if mes == 4:
    print("Abril")
if mes == 5:
    print("Mayo")
if mes == 6:
    print("Junio")
if mes == 7:
    print("Julio")
if mes == 8:
    print("Agosto")
if mes == 9:
    print("Septiembre")
if mes == 10:
    print("Octubre")
if mes == 11:
    print("Noviembre")
if mes == 12:
    print("Diciembre")

#ACTIVIDAD 12
cal1 = float(input("Calificación 1: "))
cal2 = float(input("Calificación 2: "))

promedio = (cal1 + cal2) / 2

if promedio >= 70:
    print("Aprobado")

    if promedio >= 90.0 and promedio <= 100:
        print("Desempeño excelente")

if promedio <=69.9:
    print("Reprobado")

#ACTIVIDAD 13
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura * altura)

print("IMC:", round(imc, 2))

#ACTIVDAD 14
num = int(input("Numero: "))

print(num, "x 1 =", num * 1)
print(num, "x 2 =", num * 2)
print(num, "x 3 =", num * 3)
print(num, "x 4 =", num * 4)
print(num, "x 5 =", num * 5)
print(num, "x 6 =", num * 6)
print(num, "x 7 =", num * 7)
print(num, "x 8 =", num * 8)
print(num, "x 9 =", num * 9)
print(num, "x 10 =", num * 10)

#ACTIVIDAD 15
from datetime import datetime

def mostrar_fechas():
    fecha = datetime.now()

    formato1 = fecha.strftime("%d-%m-%Y")   # dd-mm-aaaa
    formato2 = fecha.strftime("%d-%m-%y")   # dd-mm-aa
    formato3 = fecha.strftime("%d%B%Y")     # ddnombre_mesañoo

    print("Formato 1:", formato1)
    print("Formato 2:", formato2)
    print("Formato 3:", formato3)

mostrar_fechas()