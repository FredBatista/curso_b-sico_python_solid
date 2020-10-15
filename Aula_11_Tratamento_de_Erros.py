'''try:
    a = 1200/0
except:
    print("Divisão por zer, não da pra fazer")'''

'''try:
    a = 2/0
except Exception as erro:
    print("Aconteceu algum erro:", erro)'''

import Time

def abre_arquivo ():
    try:
        arquivo = open('arquivodoido.txt')
        return arquivo
    except Exception as erro:
        print("Aconteceu algum erro:", erro)
        return False
while not abre_arquivo():
    print('Tentando abrir o arquivo')
    time.sleep(5)

print("Consegui abrir o arquivo")