import requests, json, os
from getpass import getpass
from tabulate import tabulate

api_url = "https://suap.ifrn.edu.br/api/"
keys = "keys.json"

def load_credentials():
	if os.path.exists(keys):
		with open(keys, 'r') as archive:
			return json.load(archive)
	return None


def save_credentials(credentials):
	with open(keys, 'w') as archive:
		json.dump(credentials, archive)


def login():
	user = input("Matrícula: ")
	password = getpass(prompt="Senha: ")
	data = {"username": user, "password": password}
	response = requests.post(api_url+"v2/autenticacao/token/", json=data)

	if response.status_code == 200:
		token = response.json()['access']
		credentials = {"username": user, "password": password, "token": token}
		save_credentials(credentials)
		return credentials
	else:
		print("Erro na autenticação.")
		exit()


def get_token(credentials):
	return credentials['token']


def get_headers(token):
	return {"Authorization": f'Bearer {token}'}


def get_boletim(ano_letivo, periodo_letivo, headers):
	response = requests.get(api_url+f"v2/minhas-informacoes/boletim/{ano_letivo}/{periodo_letivo}/", headers=headers)

	if response.status_code == 200:
		return response.json()
	else:
		print("Erro ao obter o boletim.")
		exit()


def tabela_boletim(data):
	tabela_boletim = []
	for disciplina in data:
		linha = [
			disciplina['disciplina'],
			disciplina['media_disciplina'],
			disciplina['nota_etapa_1']['nota'],
			disciplina['nota_etapa_2']['nota'],
			disciplina['nota_etapa_3']['nota'],
			disciplina['nota_etapa_4']['nota']
		]
		tabela_boletim.append(linha)

	cabecalhos = ["Disciplina", "Média", "Nota Etapa 1", "Nota Etapa 2", "Nota Etapa 3", "Nota Etapa 4"]
	print("\n" + tabulate(tabela_boletim, headers=cabecalhos, tablefmt="grid"))


def new_token(credentials):
	user = credentials['username']
	password = credentials['password']
	data = {"username": user, "password": password}
	response = requests.post(api_url+"v2/autenticacao/token/", json=data)

	if response.status_code == 200:
		token = response.json()['access']
		credentials['token'] = token
		save_credentials(credentials)
		return credentials
	else:
		print("Erro ao renovar o token.")
		exit()


credentials = load_credentials()
if not credentials:
	credentials = login()

while (True):
	token = get_token(credentials)
	headers = get_headers(token)

	print("\n" + "="*10 + " SUAP API " + "="*10 +"\n")
	print("1. Boletim")
	print("2. Alterar Matrícula")
	print("3. Renovar Token")
	print("0. Encerrar")
	option = input("\nEscolha uma opção: ")
	print("")

	if option == "0":
		break

	if option == "1":
		print("="*10 + " BOLETIM " + "="*10)
		ano_letivo = input("Digite o Ano Letivo: ")
		periodo_letivo = input("Digite o Período: ")
		boletim = get_boletim(ano_letivo, periodo_letivo, headers)
		tabela_boletim(boletim)
		input("\n Enter.")

	if option == "2":
		print("="*10 + " ALTERAR MATRICULA " + "="*10)
		credentials = login()

	if option == "3":
		print("="*10 + " RENOVAR TOKEN " + "="*10)
		credentials = new_token(credentials)
		print("\n	Token Renovado!")
