import os
inventario = []

print("***** ESCAPE ROOM *****")
nombre = input("\nIngresa tu nombre: ")
accion = input("\nIngresa enter para continuar: ")

os.system("cls")

llaves = 0
pista1 = ""
pista2 = ""


print("Ahora se encuentra en una casa abandonada con cuatro puertas, dos puede acceder sin ningún problema, pero las otras dos necesita sus respectivas contraseñas de las puertas, en las cuales podrá obtener mediante las pistas que puede encontrar en dos de las tres habitaciones iniciales.\n")
while llaves != 5:
    print("*** HABITACIONES ***")
    print("\n1. Puerta 1")
    print("2. Puerta 2")
    print("3. Puerta 3 - PUERTA BLOQUEADA, NECESITA UNA PISTA PARA PODER ABRIRLA XD")
    print("4. Puerta 4 - PUERTA BLOQUEADA, NECESITA UNA PISTA PARA PODER ABRIRLA XD")

    opcion = int(input("\nIngrese su opción: "))

    while (opcion < 1) and (opcion > 6):
        opcion = int(input("Ingrese una opción váilda: "))

    match opcion:
        case 1:
            os.system("cls")
            print("--- Cuarto 1 ---")
            print("\n1. Acertijo 1")
            print("2. Acertijo 2")

            menu_ac = int(input("\nIngrese el acertijo a resolver: "))
            while (menu_ac < 1) or (menu_ac > 2):
                menu_ac = int(input("Ingrese una opción váilda: "))
                
            print("\n- Acertijo 1 -")
            ac1 = input("Tiene agujas pero no cose. ¿Qué es?")
            

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
    os.system("cls")

print("Felicidades acabaste de salir de la casa abandonada ")