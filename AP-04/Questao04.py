pares = 0
impares = 0

while True:
    entrada = input("Digite um número ou 'sair' para encerrar: ")

    if entrada.lower() == "sair":
        break

    numero = int(entrada)

    if numero % 2 == 0:
        pares += 1
        print(f"{numero} é par.")
    else:
        impares += 1
        print(f"{numero} é ímpar.")

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")