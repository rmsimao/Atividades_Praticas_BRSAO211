def verificar_palindromo(texto: str) -> bool:
    texto_limpo = ""

    for caractere in texto.lower():
        if caractere.isalnum():
            texto_limpo += caractere

    return texto_limpo == texto_limpo[::-1]


entrada = input("Digite uma palavra ou frase: ")

resultado = verificar_palindromo(entrada)

if resultado:
    print("Sim")
else:
    print("Não")
