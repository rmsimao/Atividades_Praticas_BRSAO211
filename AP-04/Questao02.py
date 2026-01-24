senha = input("Digite sua senha: ")

tem_numero = any(char.isdigit() for char in senha)
tem_letra = any(char.isalpha() for char in senha)

if len(senha) < 8:
    print("Senha inválida: deve ter pelo menos 8 caracteres.")
elif not tem_numero:
    print("Senha inválida: deve conter pelo menos um número.")
elif not tem_letra:
    print("Senha inválida: deve conter pelo menos uma letra.")
else:
    print("Senha válida.")
