#Fac¸a um programa que leia uma matriz de 5 linhas e 4 colunas contendo as seguintes
#informac¸oes sobre alunos de uma disciplina, sendo todas as informac¸ ˜ oes do tipo inteiro: ˜
#• Primeira coluna: numero de matr ´ ´ıcula (use um inteiro)
#• Segunda coluna: media das provas ´
#• Terceira coluna: media dos trabalhos ´
#• Quarta coluna: nota final
#Elabore um programa que:
#(a) Leia as tres primeiras informac¸ ˆ oes de cada aluno ˜
#(b) Calcule a nota final como sendo a soma da media das provas e da m ´ edia dos ´
#trabalhos
#(c) Imprima a matr´ıcula do aluno que obteve a maior nota final (assuma que so existe ´
#uma maior nota)
#(d) Imprima a media aritm ´ etica das notas finais 

lista_info_alunos = [
    [1,2,3,4],
    [5,6,7,10],
    [6,9,7,5],
    []
]
alunos_dic = []
#(a) Leia as tres primeiras informac¸ ˆ oes de cada aluno ˜
contador = 0
for i in range(3):
        salvar_dados = []
        for i in range(3):
            salvar_dados.append(lista_info_alunos[i][contador])
        contador+=1
        matricula,prova_final,trabalho_final = salvar_dados
        media_final = (prova_final + trabalho_final)/2
        alunos_dic.append({'Matricula':matricula,'Prova Final':prova_final,'Trabalho Final':trabalho_final,'Média Final':media_final})


opcao = int(input('Digite a opção que deseja: '))

if opcao==1:
      for valor in alunos_dic:
            for elemento in valor:
                if elemento=='Média Final':
                    continue
                else:
                    print(f'{elemento} : {valor[elemento]}')
            print()

if opcao==2:
     for valor in alunos_dic:
          print(f"Matrícula: {valor['Matricula']}\nMédia Final: {valor['Média Final']}\n")

if opcao==3:
    alunos_dic.sort(reverse=True,key=lambda valor:valor['Média Final'])
    print(alunos_dic[1])

if opcao==4:
    for valor in alunos_dic:
        print(f"({valor['Prova Final']} + {valor['Trabalho Final']}) / 2")