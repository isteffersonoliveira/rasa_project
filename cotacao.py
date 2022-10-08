import requests

import datetime


requisicao = requests.get("https://cdn.apicep.com/file/apicep/68537-000.json")

cep_pesquisado = requisicao.json()

estado = cep_pesquisado['state']
cidade = cep_pesquisado['city']
distrito = cep_pesquisado['district']
rua = cep_pesquisado['address']

texto = f'''
ESTADO: {estado}
CIDADE: {cidade}
DISTRITO: {distrito}
RUA: {rua}
'''

print(cep_pesquisado)

print(texto)








