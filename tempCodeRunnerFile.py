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