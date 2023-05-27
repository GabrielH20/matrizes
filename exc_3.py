#Fac¸a um programa que preenche uma matriz com o produto do valor da linha e da coluna
#de cada elemento. Em seguida, imprima na tela a matriz

def criar_tabela(linhas,colunas):
    tabela = []
    for i in range(1,colunas+1):
        elementos_tabela = []
        for k in range(1,linhas+1):
            elementos_tabela.append(i*k)
        tabela.append(elementos_tabela)
    return tabela
def imprimir_tabela(lista):
    print(*lista,sep='\n')
imprimir_tabela(criar_tabela(4,3))