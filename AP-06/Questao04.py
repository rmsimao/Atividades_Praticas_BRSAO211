import requests
from datetime import datetime

def consultar_moeda(moeda: str):
    moeda = moeda.upper()

    if moeda == "BRL":
        print("Erro: informe uma moeda estrangeira para consultar a cotação em relação ao Real (BRL).")
        return

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        dados = response.json()
        chave = f"{moeda}BRL"

        if chave not in dados:
            print("Erro: moeda não encontrada.")
            return

        cotacao = dados[chave]

        valor_atual = cotacao["bid"]
        maxima = cotacao["high"]
        minima = cotacao["low"]
        timestamp = int(cotacao["timestamp"])
        data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

        print("\nCotação da moeda em relação ao Real (BRL):")
        print(f"Moeda              : {moeda}/BRL")
        print(f"Valor atual        : R$ {valor_atual}")
        print(f"Máxima do dia      : R$ {maxima}")
        print(f"Mínima do dia      : R$ {minima}")
        print(f"Última atualização : {data_hora}")

    except requests.exceptions.RequestException:
        print("Erro na requisição. Verifique sua conexão ou tente novamente.")
    except (KeyError, ValueError):
        print("Erro ao processar os dados retornados pela API.")

if __name__ == "__main__":
    print("Consulta de cotação de moeda estrangeira em relação ao Real (BRL)")
    print("Exemplos de moedas válidas: USD, EUR, GBP, BTC")
    print("Obs: não informe BRL\n")

    moeda_digitada = input("Digite o código da moeda: ").strip()
    consultar_moeda(moeda_digitada)
