def calcula_desconto(preco_original: float, percentual_desconto: float) -> float:
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return preco_final


preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))

preco_final = calcula_desconto(preco, desconto)

print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto aplicado: {desconto:.0f}%")
print(f"Preço final com desconto: R$ {preco_final:.2f}")
