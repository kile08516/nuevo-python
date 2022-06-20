lista_alumno_isic=[
    ["Miguel Angel","Olivera Ortega","muguel@gmail.com"],
    ["Toribio salgado","marina@gmail.com","marina@gmail.com"],
    ["victor","Mateos Francisco","victor@gmail.com"],
    ["Gabriel","Garcia Dolores","gabriel@gmail.com"]
]
#print(lista_alumnos-isic)

#mostrar una lista determinado
#print(lista_alumno_isic[1])

#mostrar registro
#print(lista_alumno_isic[3][2])

#for nombres in lista_alumno_isic:
    #print(nombres[0])
    #print(nombres[1])

for alumnos in lista_alumno_isic:
    for elemento in alumnos:
        if elemento.index(elemento)==0:
            print(f"Nombre:{elemento}")
        elif alumnos.index(elemento)==1:
            print(f"apellidos:{elemento}")
        elif alumnos.index(elemento)==2:
            print(f"Correo:{elemento}")