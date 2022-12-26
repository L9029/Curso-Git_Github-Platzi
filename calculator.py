import time

#Operaciones
def plus(num1, num2):
    result = num1 + num2
    print(f"La suma de {num1} + {num2} es: {result}")

def less(num1, num2):
    result = num1 - num2
    print(f"La resta de {num1} - {num2} es: {result}")

def times(num1, num2):
    result = num1 * num2
    print(f"La multiplicación de {num1} * {num2} es: {result}")

def divide(num1, num2):
    result = num1 / num2
    print(f"La división de {num1} / {num2} es: {result}")
    
def potencia(num1, num2):
    result = num1 ** num2
    print(f"La potencia de {num1} a la {num2} es: {result}")

#Menu simple
menu = input("""
            ...Bienvenido...
                
        ¿Qué operación desea realizar?
            
        1)Suma
        2)Resta
        3)Multiplicación
        4)División
        5)Potencia
        
        Escribe -exit- para salir
        
        Seleción: """)

#Interacción con el usuario
if menu == "1":
    x = int(input("\nEliga un numero: "))
    y = int(input("\nEliga un numero: "))
    print("")
    plus(x, y)

elif menu == "2":
    x = int(input("\nEliga un numero: "))
    y = int(input("\nEliga un numero: "))
    print("")
    less(x, y)

elif menu == "3":
    x = int(input("\nEliga un numero: "))
    y = int(input("\nEliga un numero: "))
    print("")
    times(x, y)

elif menu == "4":
    x = int(input("\nEliga un numero: "))
    y = int(input("\nEliga un numero: "))
    print("")
    divide(x, y)
    
elif menu == "5":
    x = int(input("\nEliga un numero: "))
    y = int(input("\nEliga una potencia: "))
    print("")
    potencia(x, y)

elif menu == "exit":
    print("\n...Saliendo...\n")
    time.sleep(3)

else:
    print("\n...Saliendo...\n")
    time.sleep(3)
