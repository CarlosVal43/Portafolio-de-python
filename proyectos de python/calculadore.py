import sys

def sumar (num1, num2):
    return num1 + num2
def restar (num1, num2):
    return num1 - num2
def multiplicar (num1, num2):
    return num1 * num2
def dividir (num1, num2):
    
    if num1 == 0:    
        return("error, operacion invalida")

    if num2 == 0:
        return("error, operacion invalida")    
    return num1 / num2
def mi_funcion(operacion):
    operaciones_validas = ("1", "2", "3", "4")
    if operacion not in operaciones_validas:
        print(f"{operacion} ← es una operacion invalida")
        return True  # Indica que la operación es inválida
   

    


def calculadora():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. dividir")
    operacion = (input("Ingrese el numero de la operacion: "))



    
    if mi_funcion(operacion):
        sys.exit()
    else:
        pass
    while True:
        try:
            num1 = float (input("ingrese el primer numero:  "))
            break

        except ValueError:
            print(f"error, no es un numero!")

    while True:
        try:
            num2 = float (input("ingrese el segundo numero:  "))
            break

        except ValueError:
            print(f"error, no es un numero!")

            
    if operacion == "1":
        print(f"{num1} + {num2} = {sumar(num1, num2)}")
    elif operacion == "2":
        print(f"{num1} - {num2} = {restar(num1, num2)}")
    elif operacion == "3":
        print(f"{num1} x {num2} = {multiplicar(num1, num2)}")
    elif operacion == "4":
        print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Operación inválida")

calculadora()

