
alumno=input("Anota el nombre tu nombre:")
calificacion=int(input("anota tu calificacion:"))
mensaje=None
if 0<=calificacion<=69:
    mensaje="insuficiente..."
elif 70<=calificacion<=74:
    mensaje="suficiente"
elif 75<=calificacion<=84:
    mensaje="bueno..."
elif 85<=calificacion<=94:
    mensaje="notable"
elif 95<=calificacion<=100:
    mensaje="exelente"
else:
    mensaje="Calificacion no encontrada"
print(f"tienes{calificacion}de calificacion y", mensaje)


