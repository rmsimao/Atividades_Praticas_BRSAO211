import requests

def buscar_usuario_ficticio():
    url = "https://randomuser.me/api/"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # dispara exceção para erros HTTP

        dados = response.json()
        usuario = dados["results"][0]

        nome = f'{usuario["name"]["first"]} {usuario["name"]["last"]}'
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print("Usuário encontrado:")
        print(f"Nome : {nome}")
        print(f"E-mail: {email}")
        print(f"País  : {pais}")

    except requests.exceptions.RequestException:
        print("Falha ao conectar à API. Verifique sua conexão ou tente novamente.")
    except (KeyError, IndexError):
        print("Falha ao processar os dados retornados pela API.")

if __name__ == "__main__":
    buscar_usuario_ficticio()
