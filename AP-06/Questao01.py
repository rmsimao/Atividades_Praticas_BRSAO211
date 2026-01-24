import random
import string

def gerar_senha(tamanho: int) -> str:
    caracteres = (
        string.ascii_letters +   # letras maiúsculas e minúsculas
        string.digits +          # números
        string.punctuation       # símbolos
    )
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


tamanho_senha = int(input("Digite o tamanho da senha desejada: "))

if tamanho_senha < 6:
    print("Erro: recomenda-se senha com pelo menos 6 caracteres.")
else:
    senha_gerada = gerar_senha(tamanho_senha)
    print(f"Senha gerada: {senha_gerada}")
