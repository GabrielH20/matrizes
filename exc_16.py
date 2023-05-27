#Fac¸a um programa para corrigir uma prova com 10 questoes de m ˜ ultipla escolha ( ´ a, b,
#c, d ou e), em uma turma com 3 alunos. Cada questao vale 1 ponto. Leia o gabarito, e ˜
#para cada aluno leia sua matricula (numero inteiro) e suas respostas. Calcule e escreva: ´
#Para cada aluno, escreva sua matr´ıcula, suas respostas, e sua nota. O percentual de
#aprovac¸ao, assumindo m ˜ edia 7.0.

gabarito = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']

matriculas = [1, 2, 3]

respostas_alunos = [
    ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'],
    ['e', 'd', 'c', 'b', 'a', 'e', 'd', 'c', 'b', 'a'],
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
]

def corrigir_provas(gabarito,matriculas,respostas):
    for i in range(3):
        total = list(map(
            lambda x,y: 1 if x==y else 0,
            gabarito,
            respostas[i]
        ))

        if sum(total)>=7:
            status_aprovacao = 'Aprovado'
        else:
             status_aprovacao = 'Reprovado'

        print(f'Matricula: {i+1}\nNota: {sum(total)}\nTotal: {status_aprovacao}\n')

corrigir_provas(gabarito,matriculas,respostas_alunos)   

