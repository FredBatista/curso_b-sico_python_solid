'''nomes = ['Guilherme', 'Marcelo', 'João', 'Júlia']'''
'''for nome in nomes:
    print(nome)'''

'''Lista_de_números = range(5) #range não pega o extremo da esquerda, consegue especificar um intervalo'''

'''for i in range(len(nomes)): # o len quantifica quantos itens tem na coleção
    print(nomes[i])
    nomes.append('Oii')

print(nomes)'''

'''i = 0
while i < 10:
    print('I ainda é menor que 10', i)
    i = i + 1

print('Acabou o while', i)'''

'''numero = 0
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1

print('Saiu do While')'''

'''Exerciocio faça um programa que leia a quantidade de pessoas que será convidada para
 uma festa apos isso o programa irá colocar o nome de todas as pessoas
 apos isso colocar numa lista de pessoas
 Apos isso imrimir a lista de convidados
através do While'''


print('Programa de controle de festas')
print('##############################')

numero_de_convidados = input('Coloque o número de convidados: ')
Lista_de_convidados = []

i = 1
while i <= int(numero_de_convidados ): # for in range(int(numero_de_convidados)) essa observação é caso o for fosse usado
    nome_do_convidado = input('Coloque o nome do convidados # '+ str(i) +': ')
    i += 1
    Lista_de_convidados.append(nome_do_convidado)

print('Serão', numero_de_convidados, 'Convidados')

print('\nLISTA DE CONVIDADOS')
for convidado in Lista_de_convidados:
    print(convidado)





