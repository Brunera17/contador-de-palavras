def conta_palavras(frase):
    palavras = frase.split()
    print(palavras)
    return len(palavras)

frase = input("Digite uma frase: ")

print(conta_palavras(frase))