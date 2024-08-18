import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def detail_user(user):
    user_address = user["address"]
    user_address_geo = user_address["geo"]
    user_company = user["company"]

    print("="*5 + " Detalhar Usuário " + "="*5)
    print(f"Nome: {user['name']}")
    print(f"Nome de Usuário: {user['username']}")
    print(f"Email: {user['email']}")
    print(f"Telefone: {user['phone']}")
    print(f"Website: {user['website']}")
    print("Endereço")
    print(f"    Rua: {user_address['street']}")
    print(f"    Apartamento: {user_address['suite']}")
    print(f"    Cidade: {user_address['city']}")
    print(f"    CEP: {user_address['zipcode']}")
    print(f"    Geolocalização: Lat. {user_address_geo['lat']}  Lng. {user_address_geo['lng']}")
    print("Empresa")
    print(f"    Nome: {user_company['name']}")
    print(f"    Slogan: {user_company['catchPhrase']}")
    print(f"    Lema do Negócio: {user_company['bs']}")
    print("")


def list_users():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        users = response.json()
        print("="*5 + " Lista de Usuários " + "="*5)
        for user in users:
            print(f"{user['id']}. {user['name']}")
        print("")
    else:
        print("❌ Falha ao listar usuários.\n")


def list_user_todos(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        response = requests.get(f"{BASE_URL}/{user_id}/todos")
        user = requests.get(f"{BASE_URL}/{user_id}/").json()
        todos = response.json()
        print("="*5 + f" Tarefas de {user["name"]} " + "="*5)
        for todo in todos:
            status = "❌" if todo["completed"] else "⭕"
            print(f"[{status}] {todo['title']}")
        print("")
    else:
        print("❌ Usuário Not Found.\n")


def create_user():
    print("="*5 + " Criar Usuário " + "="*5)
    name = input("Nome Completo: ")
    username = input("Nome de Usuário: ")
    email = input("Email: ")

    data = {"name": name, "username": username, "email": email}
    response = requests.post(BASE_URL, json=data)

    if response.status_code == 201:
        print("⭕ Usuário criado com sucesso!\n")
    else:
        print("❌ Falha ao criar usuário.\n")


def update_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        print("="*5 + " Atualizar Usuário " + "="*5)
        user = response.json()
        print(f"Nome Atual: {user['name']}")
        name = input("Digite o novo nome: ")

        data = {"name": name}
        update_response = requests.patch(f"{BASE_URL}/{user_id}", json=data)

        if update_response.status_code == 200:
            print("⭕ Usuário atualizado com sucesso!\n")
        else:
            print("❌ Falha ao atualizar usuário.\n")
    else:
        print("❌ Usuário Not Found.\n")



def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        print("⭕ Usuário deletado com sucesso!\n")
    else:
        print("❌ Falha ao deletar usuário.\n")


def main():
    while True:
        print("="*5 + " JSON PLACEHOLDER " + "="*5)
        print("1. Listar Usuários")
        print("2. Listar Tarefas")
        print("3. CLAD de Usuários")
        print("0. Encerrar")
        option = input("\nEscolha uma opção: ")
        print("")

        if option == "0":
            break
        elif option == "1":
            list_users()
        elif option == "2":
            user_id = input("Digite o ID do Usuário: ")
            print("")
            list_user_todos(user_id)
        elif option == "3":
            print("1. Criar ")
            print("2. Ler ")
            print("3. Atualizar ")
            print("4. Deletar ")
            crud_option = input("\nEscolha uma opção: ")
            print("")

            if crud_option == "1":
                create_user()
            elif crud_option == "2":
                user_id = input("Digite o ID do Usuário: ")
                print("")

                response = requests.get(f"{BASE_URL}/{user_id}")
                if response.status_code == 200:
                    detail_user(response.json())
                else:
                    print("❌ Usuário Not Found.\n")

            elif crud_option == "3":
                user_id = input("Digite o ID do Usuário: ")
                print("")

                update_user(user_id)
            elif crud_option == "4":
                user_id = input("Digite o ID do Usuário: ")
                print("")

                delete_user(user_id)
        else:
            print("❌ Opção inválida.\n")

        input("Pressione Enter para continuar...")
        print("")


if __name__ == "__main__":
    main()
