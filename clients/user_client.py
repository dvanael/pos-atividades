from user_wrapper import UserAPI

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
    try:
        users = UserAPI.list_users()
        print("="*5 + " Lista de Usuários " + "="*5)
        for user in users:
            print(f"{user['id']}. {user['name']}")
        print("")
    except Exception as e:
        print(f"❌ {str(e)}\n")


def list_user_todos(user_id):
    try:
        todos = UserAPI.list_user_todos(user_id)
        user = UserAPI.get_user(user_id)
        print("="*5 + f" Tarefas de {user['name']} " + "="*5)
        for todo in todos:
            status = "❌" if todo["completed"] else "⭕"
            print(f"[{status}] {todo['title']}")
        print("")
    except Exception as e:
        print(f"❌ {str(e)}\n")


def create_user():
    print("="*5 + " Criar Usuário " + "="*5)
    name = input("Nome Completo: ")
    username = input("Nome de Usuário: ")
    email = input("Email: ")

    try:
        user = UserAPI.create_user(name, username, email)
        print("⭕ Usuário criado com sucesso!\n")
    except Exception as e:
        print(f"❌ {str(e)}\n")


def update_user(user_id):
    try:
        user = UserAPI.get_user(user_id)
        print(f"Nome Atual: {user['name']}")
        name = input("Digite o novo nome: ")

        user = UserAPI.update_user(user_id, name)
        print("⭕ Usuário atualizado com sucesso!\n")
    except Exception as e:
        print(f"❌ {str(e)}\n")


def delete_user(user_id):
    try:
        if UserAPI.delete_user(user_id):
            print("⭕ Usuário deletado com sucesso!\n")
    except Exception as e:
        print(f"❌ {str(e)}\n")


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
            print("1. Criar")
            print("2. Ler")
            print("3. Atualizar")
            print("4. Deletar")
            crud_option = input("\nEscolha uma opção: ")
            print("")

            if crud_option == "1":
                create_user()

            elif crud_option == "2":
                user_id = input("Digite o ID do Usuário: ")
                print("")
                try:
                    user = UserAPI.get_user(user_id)
                    detail_user(user)
                except Exception as e:
                    print(f"❌ {str(e)}\n")

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
