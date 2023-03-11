import random
opcion = ["piedra", "papel", "tijeras"]
def user():
    option_user= input("Elige y escribe una de estas opciones \n piedra \n papel \n tijeras ").lower()
    option_machine = random.choice(opcion)
    print(option_machine)
    if option_user not in opcion:
        print("opcio no valida")
        user()
    else:
        comparacion(option_machine, option_user)

def comparacion(var,var2):
    #empate
    
    if var == var2:
        print("Empate")
    elif var == "piedra" and var2 == "tijeras":
        print("Mac gano")
    elif var == "papel" and var2 == "piedra":
        print("Mac gano")
    elif var == "tijeras" and var2 == "papel":
        print("Mac gano")
    else:
        print("Humano gano")

#user()

def jugar():
    while True:
        user()
        res = input("ingrese 'S' para volver a jugar o 'N' para terminar: ")
        if res != "s":
            break

jugar()