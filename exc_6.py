#Leia uma matriz 5 x 5. Leia tambem um valor ´ X. O programa devera fazer uma busca ´
#desse valor na matriz e, ao final, escrever a localizac¸ao (linha e coluna) ou uma mensa- ˜
#gem de “nao encontrado”.

lista_um = [
    [2,5,7,10],
    [24,52,79,12],
    [26,15,38,60],
    [21,5,35,120]
]

lista_dois = [
    [2,56,71,10],
    [24,62,89,22],
    [16,25,0,40],
    [1,5,37,720]
]

lista_tres = list(map(
    lambda valor_um,valor_dois: valor_um if valor_um>=valor_dois else valor_dois,
    lista_um,
    lista_dois
))
print(lista_tres)

