import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = input("Digite seu usuário: ")
password = getpass()
  
response = requests.get('https://api.github.com/user/followers', auth=HTTPBasicAuth(user, password))

# ver seguidores
followers = response.json()  
for i, follower in enumerate(followers, ):
    print(f"{i} - {follower['login']}")


# seguir usuário
username = input("Digite o login do usuário para seguir: ")
response = requests.put(f'https://api.github.com/user/following/{username}', auth=HTTPBasicAuth(user, password))

if response.status_code == 204:
    print(f"Seguiu {username}")
else:
    print("Erro!")


# parando de seguir
response = requests.delete(f'https://api.github.com/user/following/{username}', auth=HTTPBasicAuth(user, password))

if response.status_code == 204:
    print(f"Parou de seguir {username}.")
else:
    print("Erro!")
