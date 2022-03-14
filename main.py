import requests

link = 

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())