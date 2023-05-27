#Leia uma matriz de 3 x 3 elementos. Calcule e imprima a sua transposta.
lista = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for valor in lista:
    valor.sort()

nova_lista =[]

contador=0
for i in range(3):
    guardar = []
    for elemento in lista:
        guardar.append(elemento[contador])
    nova_lista.append(guardar)
    contador+=1

print(*nova_lista,sep='\n')
    