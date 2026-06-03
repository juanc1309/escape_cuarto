import os
inventario = []

print("***** ESCAPE ROOM *****")
nombre = input("\nIngresa tu nombre: ")
accion = input("\nIngresa enter para continuar: ")

os.system("cls")

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

    while (opcion < 1) or (opcion > 6):
        opcion = int(input("Ingrese una opción váilda: "))

    match opcion:
        case 1:
            os.system("cls")
            print("--- Cuarto 1 ---")

            print("\n- Acertijo 1 -")
            ene agujas pero no cose. ¿Qué es?")

        case 2:
            os.system("cls")
            print("--- Cuarto 2 ---")
            print("\n- Acertijo 1 -")
            print("")

        case 3:
            if pista1 is "Aunque comience por la noche, termino casi por la mañana. ¿Qué soy?":
                os.system("cls")
                print("--- Cuarto 3 ---")
                print("\n- Acertijo 1 -")
                print("")
            else:
                print("Aun no tienes la llave, intentalo cuando lo tengas")

        case 4:
            if pista1 is "Aunque comience por la noche, termino casi por la mañana. ¿Qué soy?":
                os.system("cls")
                print("--- Cuarto 4 ---")
                print("\n- Acertijo 1 -")
                print("")
            else:
                print("Aun no tienes la llave, intentalo cuando lo tengas")

print("Felicidades acabaste de salir de la casa abandonada ")