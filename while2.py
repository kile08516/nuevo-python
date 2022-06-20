

while True:
    nombre_alumno=input("Anota el nombre del alumno:")
    apellido_alumno=input("Anota el apellido paterno:")
    edad_alumno=input("Anota la edad:")

    print(f"Alumno:{nombre_alumno},{apellido_alumno},{edad_alumno}registrado corectamente")

    condicion=input("¿desea hacer otro registro?(S=si N=no):")
    if condicion =="n" or condicion=="N":
        break
print("Alumnos regist4rados corretamente")