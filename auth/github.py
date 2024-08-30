import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

url = "https://api.github.com/user/"

def following_url(username):
	return url + f"following/{username}"

def followers_url():
	return url + "followers"

def list_followers(login, password):
	response = requests.get(followers_url(), auth=HTTPBasicAuth(login, password))
	if response.status_code == 200:	
		followers = response.json()  
		for i, follower in enumerate(followers):
			print(f"{i} - {follower['login']}")
	else:
		print("\nErro!")


def follow_user(login, password):
	username = input("Digite o login do usuário para seguir: ")
	print(following_url(username))
	response = requests.put(following_url(username), auth=HTTPBasicAuth(login, password))

	if response.status_code == 204:
		print(f"Seguiu {username}")
	else:
		print("\nErro!")


def unfollow_user(login, password):
	username = input("Digite o login do usuário para unfollow: ")
	response = requests.delete(following_url(username), auth=HTTPBasicAuth(login, password))

	if response.status_code == 204:
		print(f"Parou de seguir {username}")
	else:
		print("\nErro!")


def set_login_and_token():
	login = input("Digite seu login: ")
	access_token = getpass(prompt="Access Token: ")
	return login, access_token


username = None
while(True):
	print("")
	print("="*10 + " GITHUB API " + "="*10 +"\n")
	
	if username == None or access_token == None:
		username, access_token = set_login_and_token()
		print("")
	else:
		print(f"Logado com {username}\n")

	print("1. Listar seus seguidores")
	print("2. Seguir usuário")
	print("3. Unfollow usuário")
	print("4. Atualizar login")
	print("0. Encerrar")
	option = input("\nEscolha uma opção: ")
	print("")

	if option == "0":
		break

	if option == "1":
		print("="*10 + " LISTA DE USUÁRIOS " + "="*10)
		list_followers(username, access_token)

	if option == "2":
		print("="*10 + " SEGUIR USUÁRIO " + "="*10)
		follow_user(username, access_token)

	if option == "3":
		print("="*10 + " UNFOLLOW USUÁRIOS " + "="*10)
		unfollow_user(username, access_token)

	if option == "4":
		print("="*10 + " ATUALIZAR LOGIN " + "="*10)
		username, access_token = set_login_and_token()
