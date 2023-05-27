#Fac¸a um programa para gerar automaticamente numeros entre 0 e 99 de uma cartela de ´
#bingo. Sabendo que cada cartela devera conter 5 linhas de 5 n ´ umeros, gere estes dados ´
#de modo a nao ter n ˜ umeros repetidos dentro das cartelas. O programa deve exibir na ´
#tela a cartela gerada.
from random import randint
def imprimir_valor(lista):
    print(*lista,sep='\n')

def preencher_numeros(colunas=5,linhas=5):

    cartela_bingo = []
    numeros_na_cartela = []

    for i in range(colunas):

        preencher = []

        for i in range(linhas):

            while True:

                numero_aleatorio = randint(0,99)
                if numero_aleatorio not in numeros_na_cartela:
                    break

            preencher.append(numero_aleatorio)
            numeros_na_cartela.append(numero_aleatorio)

        cartela_bingo.append(preencher)
        
    return cartela_bingo

imprimir_valor(preencher_numeros())
