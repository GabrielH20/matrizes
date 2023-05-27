#Fac¸a um programa que leia duas matrizes A e B de tamanho 3 x 3 e calcule C = A ∗ B.
#Fac¸a um programa que leia uma matriz A de tamanho 3 x 3 e calcule B = A2

# Matriz A
matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matriz B
matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

#Matriz C
def imprimir_matriz(matriz):
    print(*matriz,sep='\n')
    print()

def multiplicar_matrizes(matriz_a,matriz_b):
    matriz_c = []
    for i in range(3):
        mapear_matrizes = list(map(
            lambda x,y:x*y,
            matriz_a[i],
            matriz_b[i]
        ))
        matriz_c.append(mapear_matrizes)
    return matriz_c
#Matriz D
def elevar_matrizes(matriz_a,matriz_b):
    matriz_d = []
    for i in range(3):
        mapear_matrizes_dois = list(map(
            lambda x,y:y**x,
            matriz_a[i],
            matriz_b[i]
        ))
        matriz_d.append(mapear_matrizes_dois)
    return matriz_d

imprimir_matriz(multiplicar_matrizes(matriz_a,matriz_b))
imprimir_matriz(elevar_matrizes(matriz_a,matriz_b))