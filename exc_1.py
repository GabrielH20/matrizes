#Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.

lista = [
    [10,10,11,10],
    [10,10,11,10],
    [10,10,11,10],
    [10,10,11,10]
]

total = 0
for valor in lista:
    for numero in valor:
        if numero>10:
            total+=1
print(total)