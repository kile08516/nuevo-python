
from Alumno import *

persona1=Persona("Nicolas","Guzman"30)
print("me llamo",persona1.nombre)
print("mis apellidos",persona1.apellidos)
print("y tengo",persona1.edad"Años")
persona1.comer()
persona1.caminando()

alumno1=Alumno("Miguel","S0202201")
print(alumno1.promedio())
print(alumno1.comer())

mi_archivo=open("persona.txt","w")
try
    mi_archivo.write(f"esta es una persona {alumno1.nombre}n")
    mi_archivo.write(f"otra {alumno1.nombre}n")
finally:
    mi_archivo.close()


