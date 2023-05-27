#Fac¸a um programa que permita ao usuario entrar com uma matriz de 3 x 3 n ´ umeros ´
#inteiros. Em seguida, gere um array unidimensional pela soma dos numeros de cada ´
#coluna da matriz e mostrar na tela esse array

lista_numeros = [
    [5,6,10],
    [-3,1,-12],
    [23,5,12]
]
contador = 0
armazenar_resposta =[]

for i in range(3):

    valor_coluna = []

    for valor in lista_numeros:
        valor_coluna.append(valor[contador])
    
    armazenar_resposta.append(sum(valor_coluna))

    contador+=1

print(armazenar_resposta)