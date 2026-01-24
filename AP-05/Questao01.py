def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    return valor_conta * (porcentagem_gorjeta / 100)


valor_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta (%): "))

valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
valor_total = valor_conta + valor_gorjeta

print(f"Valor da conta: R$ {valor_conta:.2f}")
print(f"Gorjeta ({porcentagem_gorjeta:.0f}%): R$ {valor_gorjeta:.2f}")
print(f"Valor total a pagar: R$ {valor_total:.2f}")
