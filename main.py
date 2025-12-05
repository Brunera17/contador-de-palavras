from contador import conta_palavras

frase = input("Digite uma frase: ")
quantidade = conta_palavras(frase)
print("")
print(f"A frase contém {quantidade} palavras.")