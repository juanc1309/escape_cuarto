import os
inventario = []

print("***** ESCAPE ROOM *****")
nombre = input("\nIngresa tu nombre: ")
accion = input("\nIngresa enter para continuar: ")

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

llaves = 0
pista1 = ""
pista2 = ""

while llaves != 5:
    print("Ahora se encuentra en una casa abandonada con cinco puertas, tres puede acceder sin ningún problema, mas sin embargo las otras dos necesita sus respectivas contraseñas de las puertas, en las cuales podrá obtener mediante las pistas que puede encontrar en dos de las tres habitaciones iniciales.")
    print("\n*** HABITACIONES ***")
    print("\n1. Puerta 1")
    print("2. Puerta 2")
    print("3. Puerta 3")
    print("4. Puerta 4 - PUERTA BLOQUEADA, NECESITA UNA PISTA PARA PODER ABRIRLA XD")
    print("5. Puerta 5 - PUERTA BLOQUEADA, NECESITA UNA PISTA PARA PODER ABRIRLA XD")

    opcion = int(input("\nIngrese su opción: "))

    match opcion:
        case 1:

        case 2:

        case 3:

        case 4:
            if pista1 is "":
                
        case 5:

        case _: