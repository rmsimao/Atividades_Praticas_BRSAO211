temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Unidade de origem (C, F ou K): ").upper()
unidade_destino = input("Unidade de destino (C, F ou K): ").upper()

if unidade_origem == unidade_destino:
    temperatura_convertida = temperatura

elif unidade_origem == "C":
    if unidade_destino == "F":
        temperatura_convertida = (temperatura * 9/5) + 32
    elif unidade_destino == "K":
        temperatura_convertida = temperatura + 273.15
    else:
        print("Unidade de destino inválida.")
        exit()

elif unidade_origem == "F":
    if unidade_destino == "C":
        temperatura_convertida = (temperatura - 32) * 5/9
    elif unidade_destino == "K":
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
    else:
        print("Unidade de destino inválida.")
        exit()

elif unidade_origem == "K":
    if unidade_destino == "C":
        temperatura_convertida = temperatura - 273.15
    elif unidade_destino == "F":
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
    else:
        print("Unidade de destino inválida.")
        exit()

else:
    print("Unidade de origem inválida.")
    exit()

print(f"Temperatura original: {temperatura:.2f}°{unidade_origem}")
print(f"Temperatura convertida: {temperatura_convertida:.2f}°{unidade_destino}")
