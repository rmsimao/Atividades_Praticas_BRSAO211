num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")

elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")

elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")

elif operacao == "/":
    if num2 == 0:
        print("Erro: divisão por zero não é permitida.")
    else:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")

else:
    print("Operação inválida.")
