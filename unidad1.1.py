#8.- sentencia if else


calificacionProgramacion=float(input("introduce la calificacion de programacion: "))
calificacionRedes=float(input("introduce la calificacion de Redes: "))
calificacionMatematicas=float(input("introduce la calificacion de matematicas: "))
promedioCalificaciones=(calificacionProgramacion+calificacionRedes+calificacionMatematicas)/3
if promedioCalificaciones>=70:
    print("Aprobado: ", promedioCalificaciones)
else:
    print("Debes estudiar mas,Estas reprobado: ",promedioCalificaciones)