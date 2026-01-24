from datetime import date

try:
    ano = int(input("Digite o ano de nascimento: "))
    mes = int(input("Digite o mês de nascimento (1 a 12): "))
    dia = int(input("Digite o dia de nascimento: "))

    data_nascimento = date(ano, mes, dia)
    data_atual = date.today()

    if data_nascimento > data_atual:
        print("Erro: a data de nascimento não pode ser no futuro.")
    else:
        dias_vivo = (data_atual - data_nascimento).days
        print(f"Você está vivo há {dias_vivo} dias.")

except ValueError:
    print("Erro: data inválida. Verifique o dia, mês e ano informados.")
