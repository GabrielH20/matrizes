#Fac¸a um programa que leia duas matrizes 2 x 2 com valores reais. Oferec¸a ao usuario ´
#um menu de opc¸oes: ˜
#(a) somar as duas matrizes
#(b) subtrair a primeira matriz da segunda
#(c) adicionar uma constante as duas matrizes `
#(d) imprimir as matrizes

matriz_um = [
    [1,2],
    [3,4]
]

matriz_dois = [
    [5,6],
    [7,8]
]

#A E B
def operacao_com_matrizes(matriz_um,matriz_dois,somar_matrizes=False,diminuir_matrizes=False):
    matriz_tres = []
    for y in range(len(matriz_um)):
        linha = []
        for i in range(len(matriz_um)):
            if somar_matrizes==True:
                valor_adicionar = matriz_um[y][i] + matriz_dois[y][i]
            if diminuir_matrizes==True:
                valor_adicionar = matriz_dois[y][i] - matriz_um[y][i] 
            linha.append(valor_adicionar)
        matriz_tres.append(linha)
    return matriz_tres

#C
def adicionar_constante_matriz(matriz,constante):
    for valor in matriz:
        for i in range(len(valor)):
            salvar_valor = valor.pop(i)
            valor.insert(i,salvar_valor+constante)
    return matriz

#D
def imprimir_matriz(matriz):
    print(*matriz,sep='\n')
    print()
    
imprimir_matriz(operacao_com_matrizes(matriz_um,matriz_dois,diminuir_matrizes=True))
imprimir_matriz(adicionar_constante_matriz(matriz_um,3))
