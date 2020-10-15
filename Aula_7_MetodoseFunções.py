''''#() sempre que tiver parenteses, é uma função. O que fica dentro dos parenteses, são parâmetros
'''
'''
def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

if tem_sete_itens([1,2,3,4,5,6,7,8,9]):
    print('Realmente tem 7 itens')'''

'''Exercicio
Escreva uma função que recebe um objeto de coleção e retorna o valor do maior número dessa coleção
faça outra função que retona o menor número'''

def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

print(maior([1,70,9,10,6,15,22,35]))

def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item
print(menor([-5,0,6,10,6,8,-20]))



