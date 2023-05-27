#. Fac¸a programa que leia uma matriz 3 x 6 com valores reais.
#(a) Imprima a soma de todos os elementos das colunas ´ımpares.
#(b) Imprima a media aritm ´ etica dos elementos da segunda e quarta colunas. ´
#(c) Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.
#(d) Imprima a matriz modificada.
from itertools import product,combinations
matriz = [
    [1.5, 2.0, 3.5, 4.0, 5.5, 6.0],
    [2.5, 3.0, 4.5, 5.0, 6.5, 7.0],
    [3.5, 4.0, 5.5, 6.0, 7.5, 8.0]
]

lista_colunas = []

contador=0
for i in range(6):
    coluna = []
    for valor in matriz:
        coluna.append(valor[i])
    lista_colunas.append(coluna)

print(*lista_colunas,sep='\n')

#A e B
valor_soma = 0
valor_media = 0
for i in range(len(lista_colunas)):
    if i%2!=0:
        valor_soma+=sum(lista_colunas[i])
    
    if i in [2,4]:
        valor_media+=sum(lista_colunas[i])

media_aritimetica_2_4 = valor_media /2
print(media_aritimetica_2_4)
print(valor_soma)

#C
guardar = list(map(
    lambda valor_um,valor_dois:valor_um+valor_dois,
    lista_colunas[0],
    lista_colunas[1]
))

lista_colunas.pop()
lista_colunas.append(guardar)
print(*lista_colunas,sep='\n')
