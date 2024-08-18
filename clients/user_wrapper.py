import requests

class UserAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com/users"

    @classmethod
    def list_users(cls):
        response = requests.get(cls.BASE_URL)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Erro ao listar usuários.")


    @classmethod
    def get_user(cls, user_id):
        response = requests.get(f"{cls.BASE_URL}/{user_id}")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Usuário Not Found.")


    @classmethod
    def create_user(cls, name, username, email):
        data = {"name": name, "username": username, "email": email}
        response = requests.post(cls.BASE_URL, json=data)
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception("Erro ao criar usuário.")


    @classmethod
    def update_user(cls, user_id, name=None, username=None, email=None):
        data = {}
        if name: data["name"] = name
        if username: data["username"] = username
        if email: data["email"] = email

        response = requests.patch(f"{cls.BASE_URL}/{user_id}", json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Erro ao atualizar usuário.")


    @classmethod
    def delete_user(cls, user_id):
        response = requests.delete(f"{cls.BASE_URL}/{user_id}")
        if response.status_code == 200:
            return True
        else:
            raise Exception("Erro ao deletar usuário.")


    @classmethod
    def list_user_todos(cls, user_id):
        response = requests.get(f"{cls.BASE_URL}/{user_id}/todos")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Erro ao listar tarefas do usuário.")


