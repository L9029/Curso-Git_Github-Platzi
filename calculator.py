import time

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

menu = input("""
            ...Bienvenido...
                
        ¿Qué operación desea realizar?
            
        1)Suma
        2)Resta
        3)Multiplicación
        4)División
        
        Escribe -exit- para salir
        
        Seleción: """)

if menu == 1:
    pass

elif menu == 2:
    pass

elif menu == 3:
    pass

elif menu == 4:
    pass

elif menu == "exit":
    print("\n...Saliendo...\n")
    time.sleep(5)