import os

llaves = 0
pista1 = ""
pista2 = ""
n_ac = 0
ac1 = ""

print("***** ESCAPE ROOM *****")
nombre = input("\nIngresa tu nombre: ")
os.system("cls")

print(nombre.capitalize(), "ahora se encuentra en una casa abandonada con cuatro puertas, dos puede acceder sin ningún problema, pero las otras dos necesita sus respectivas contraseñas de las puertas, en las cuales podrá obtener mediante las pistas que puede encontrar en dos de las tres habitaciones iniciales.\n")
while llaves != 5:
    print("*** HABITACIONES ***")
    print("\n1. Puerta 1")
    print("2. Puerta 2")
    print("3. Puerta 3 - PUERTA BLOQUEADA, NECESITA UNA PISTA PARA PODER ABRIRLA XD")
    print("4. Puerta 4 - PUERTA BLOQUEADA, NECESITA UNA PISTA PARA PODER ABRIRLA XD")

    opcion = int(input("\nIngrese su opción: "))

    while (opcion < 1) or (opcion > 5):
        opcion = int(input("\nIngrese una opción váilda: "))

    match opcion:
        case 1:
            os.system("cls")
            
            print("--- Cuarto 1 ---")
            if (ac1.lower() == "reloj") or (ac1.lower() == "el reloj"):
                print("1. Acertijo 1 - COMPLETADO")
            else:
                print("\n1. Acertijo 1")
            print("2. Acertijo 2")
            print("3. Acertijo 3")

            menu_ac = int(input("\nIngrese el acertijo a resolver: "))
            while (menu_ac < 1) or (menu_ac > 3):
                menu_ac = int(input("Ingrese una opción váilda: "))

            match menu_ac:
                case 1:
                    os.system("cls")
                    print("- Acertijo 1 -")
                    if (ac1.lower() == "reloj") or (ac1.lower() == "el reloj"):
                        print("El acertijo ha sido resuelto, haga otro acertijo")
                        input("Presione enter para continuar: ")
                    else: 
                        ac1 = input("Tiene agujas pero no cose. ¿Qué es?: ")
                        if (ac1.lower() == "reloj") or (ac1.lower() == "el reloj"):
                            n_ac = n_ac + 1
                            print("Correcto ahora faltan ", (3 - n_ac) ," acertijos más ")
                            input("Presione enter para continuar: ")
                        else:
                            print("Incorreto, sigue intentandolo o haz otro arcetijo: ") 
                            input("Presione enter para continuar: ")
                        

                case 2:
                    os.system("cls")
                    print("- Acertijo 2 -")
                    ac2 = input("Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera.")
                case 3:
                    os.system("cls")
                    print("- Acertijo 3 -")
                    ac3 = input("Tengo ciudades pero no casas, montañas pero no árboles y agua pero no peces. ¿Qué soy?")

        case 2:
            os.system("cls")
            print("--- Cuarto 2 ---")
            print("\n- Acertijo 1 -")
            print("")

        case 3:
            if pista1 == "Aunque comience por la noche, termino casi por la mañana. ¿Qué soy?":
                os.system("cls")
                print("--- Cuarto 3 ---")
                print("\n- Acertijo 1 -")
                print("")
            else:
                os.system("cls")
                print("Aun no tienes la pista, intentalo cuando lo tengas")
                input("\nPresione cualquier tecla para salir: ")

        case 4:
            if pista1 == "Aunque comience por la noche, termino casi por la mañana. ¿Qué soy?":
                os.system("cls")
                print("--- Cuarto 4 ---")
                print("\n- Acertijo 1 -")
                print("")
            else:
                os.system("cls")
                print("Aun no tienes la pista, intentalo cuando lo tengas")
                input("\nPresione cualquier tecla para salir: ")

    os.system("cls")

print("Felicidades acabaste de salir de la casa abandonada ")