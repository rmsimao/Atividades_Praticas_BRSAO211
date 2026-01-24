import requests

def buscar_usuario():
    url = "https://randomuser.me/api/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()

        dados = resposta.json()
        usuario = dados["results"][0]

        nome = f'{usuario["name"]["first"]} {usuario["name"]["last"]}'
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print("Usuário encontrado:")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException:
        print("Falha ao conectar à API. Verifique sua conexão ou tente novamente.")

if __name__ == "__main__":
    buscar_usuario()
