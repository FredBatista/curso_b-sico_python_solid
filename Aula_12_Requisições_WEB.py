import requests


cabecalho = {'User-agent': 'Windows 12 ',
             'Referer': 'https://google.com'}

meus_cookies = {'Ultima-Visita':'10-10-2020'}
texto =None
try:
    requisicao = requests.post('https://putsreq.com/GUab3BSI65KSgiuZr639',
                              headers=cabecalho,
                               cookies=meus_cookies)
    texto = requisicao.text
except Exception as e:
    print("Requisição deu erro",e)
print(texto)

