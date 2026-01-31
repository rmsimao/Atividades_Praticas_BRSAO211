import requests

def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        dados = response.json()
        
        if dados.get("erro"):
            print("Falha: CEP não encontrado.")
            return

        logradouro = dados.get("logradouro", "Não informado")
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "Não informado")
        estado = dados.get("uf", "Não informado")

        print("Endereço encontrado:")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro    : {bairro}")
        print(f"Cidade    : {cidade}")
        print(f"Estado    : {estado}")

    except requests.exceptions.RequestException:
        print("Falha na requisição. Verifique sua conexão e tente novamente.")
    except ValueError:
        print("Falha ao processar a resposta da API.")

if __name__ == "__main__":
    cep_digitado = input("Digite o CEP (apenas números): ").strip()
    consultar_cep(cep_digitado)
