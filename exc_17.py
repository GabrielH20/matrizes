#Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. Em seguida, escreva
#o numero de alunos cuja pior nota foi na prova 1, o n ´ umero de alunos cuja pior nota foi ´
#na prova 2, e o numero de alunos cuja pior nota foi na prova 3. Em caso de empate ´
#das piores notas de um aluno, o criterio de desempate ´ e arbitr ´ ario, mas o aluno deve ser ´
#contabilizado apenas uma vez.
notas = [
    [7.5, 8.0, 6.5],
    [6.0, 7.0, 7.0],
    [8.0, 6.5, 7.5],
    [7.0, 6.5, 7.0],
    [6.5, 7.0, 6.0],
    [8.5, 8.5, 8.0],
    [7.0, 7.5, 6.5],
    [6.0, 6.0, 6.5],
    [7.5, 4.0, 4.0],
    [6.5, 7.0, 7.0]
]

conjunto = [[],[],[]]
for lista in notas:
    valor_indece = lista.index(min(lista))
    conjunto[valor_indece].append(1)

for i in range(3): 
    print(f'Quantidade alunos da prova {i+1}: {sum(conjunto[i])}')