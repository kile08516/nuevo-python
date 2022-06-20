

lista_nombres=["Diana","Vctor","Bruno","Gabriel"]
lista_numeros=[2,8,12,1,9]
print(lista_nombres)
print(lista_numeros)

print(len(lista_nombres))
print(lista_nombres[2])

print(lista_nombres[2][3])
lista_nombres.insert(3,"Cira")

print(lista_nombres)
for elementos in lista_nombres:
    print(elementos)

lista_nombres.append("Miguel")
print(lista_nombres)

lista_nombres.pop()
print(lista_nombres)

#ordenador
lista_numeros.sort()
print(lista_numeros)
