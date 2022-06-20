

edad=int(input("anota tu edad:"))
mensaje=None
if 0<=edad<10:
    mensaje="la infancia es increible..."
elif 10<=edad<=20:
    mensaje="muchos cambios, mucho estudio..."
elif 20<=edad<30:
    mensaje="amor y mucho trabajo..."
elif 40<=edad<=50:
    mensaje=" estas en las ultimas..."
else:
    mensaje="edad no encontrada, estas ruco"
print(f"tienes {edad} años de edad",mensaje )
