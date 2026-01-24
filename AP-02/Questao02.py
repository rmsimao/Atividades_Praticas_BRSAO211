produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"Produto: {produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto aplicado: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
