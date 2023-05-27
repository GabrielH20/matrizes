#Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
#elementos. Escreva ao final a matriz obtida.
from copy import deepcopy
lista=[]
adicionar_zero = [0 for i in range(5)]
for i in range(5):
    lista.append(deepcopy(adicionar_zero))
for i in range(5):
    lista[i].insert(i,1)
    lista[i].pop()
print(*lista,sep='\n')

