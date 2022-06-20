import paquetes_funciones

paquetes_funciones.menu()

opcion = int(input("Anota una opcion(1=suma,2=resta,3=multiplicacion,4=divicion:"))
numero1 = int(input("Anota un numero:"))
numero2 = int(input("anota otro numero"))

opcion == int(input("¿desea hacer otro registro?(S=si N=no):"))
if opcion == 1:
    print(paquetes_funciones.suma(numero1, numero2))
elif opcion == 2:
    print(paquetes_funciones.resta(numero1, numero2))
if opcion == 3:
    print(paquetes_funciones.multiplicacion(numero1, numero2))
elif opcion == 4:
    print(paquetes_funciones.divicion(numero1, numero2))
