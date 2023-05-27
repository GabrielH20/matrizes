#Leia uma matriz 4 x 4, imprima a matriz e retorne a localizac¸ao (linha e a coluna) do ˜
#maior valor.
lista = [
    [1,2,3,4],
    [100,10,11,10],
    [10,10,15,10],
    [10,10,11,90]
]
valor_anterior = 0
for valor in lista:
    for elemento in valor:
        if elemento>=valor_anterior:
            valor_anterior=elemento
            indece_lista = lista.index(valor)
            indece_elemento = valor.index(elemento)
print(valor_anterior,indece_lista,indece_elemento)