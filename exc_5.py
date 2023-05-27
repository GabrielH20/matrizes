#Leia uma matriz 5 x 5. Leia tambem um valor ´ X. O programa devera fazer uma busca ´
#desse valor na matriz e, ao final, escrever a localizac¸ao (linha e coluna) ou uma mensa- ˜
#gem de “nao encontrado”.

lista = [
    [1,2,3,4],
    [100,110,11,80],
    [30,10,125,60],
    [10,50,115,690]
]

x = 60    
def procurar_valor_lista(lista,x):
    for elemento in lista:
        for valor in elemento:
            if valor==x:
                indice_coluna = lista.index(elemento)
                indice_linhas = elemento.index(valor)
                return f'O valor {x} está na coluna: {indice_coluna} na linha: {indice_linhas}'
    else:
        return f'Valor {x} não encontrado'
    
print(procurar_valor_lista(lista,69))