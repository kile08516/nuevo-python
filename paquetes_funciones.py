

def menu():
    print("desea hacer un ajuste, opcion")
    print("para suma")
    print("para resta")
    print("para multiplicacion")
    print("para divicion")
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def divicion(a,b):
    return a/b
def salido(nombre):
    return f"hola desde una funcion,{nombre}"

def validadndo_opciones():
   opcion = int(input("Anota una opcion(1=suma,2=resta,3=multiplicacion,4=divicion:"))
   numero1 = int(input("Anota un numero:"))
   numero2 = int(input("anota otro numero"))
   if opcion == 1:
    print(suma(numero1, numero2))
   elif opcion == 2:
    print(resta(numero1, numero2))
   elif opcion == 3:
    print(multiplicacion(numero1, numero2))
   elif opcion == 4:
    print(divicion(numero1, numero2))
