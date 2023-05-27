# Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estao acima da ˜
#diagonal principal.

lista = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
total = 0
def calcular_elementos_linha(lista,localizacao_elemento,diagoniaL_tipo):
    global total

    if diagoniaL_tipo=='Principal':
        indece_valor=0
    else:
        indece_valor=2

    for elemento in lista:
        for indece,valor in enumerate(elemento):
            
            if indece<indece_valor and localizacao_elemento=='Abaixo':
                total+=valor

            if indece>indece_valor and localizacao_elemento=='Acima':
                total+=valor

            if indece==indece_valor and localizacao_elemento=='Meio':
                total+=valor

        if diagoniaL_tipo=='Principal':
            indece_valor+=1
        else:
            indece_valor-=1
    return total

print(calcular_elementos_linha(lista,'Meio','a'))
