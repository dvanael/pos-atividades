import requests
import json
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

user = input("matricula: ")
password = getpass(prompt="senha: ")

data = {"username":user,"password":password}

response = requests.post(api_url+"v2/autenticacao/token/", json=data)
token = response.json()['access']
# print(response.json())

headers = {
    "Authorization": f'Bearer {token}'
}


ano_letivo = input("Digite o Ano Letivo:")
periodo_letivo = input("Digite o Periodo:")
response = requests.get(api_url+f"v2/minhas-informacoes/boletim/{ano_letivo}/{periodo_letivo}/", headers=headers).json()

# print(response.text)

for disciplina in response:
    print(f"Média {disciplina['media_disciplina']} - {disciplina['disciplina']}")
