def conta_palavras(frase):
    palavras = frase.split()
    print(palavras)
    return len(palavras)

frase = input("Digite uma frase: ")
print("")
print(f"Quantidade de palavras: {conta_palavras(frase)}")