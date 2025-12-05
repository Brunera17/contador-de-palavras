from contador import conta_palavras

frase = input("Digite uma frase: ").strip()
if not frase:
    print("Erro: A frase não pode ser vazia.")
else:
    resultado = conta_palavras(frase)
    if resultado:
        print("Contagem de palavras:")
        for palavra, quantidade in resultado.items():
            print(f"{palavra}:{quantidade}")
    else:
        print(f"Nenhuma palavra válida foi encontrada.")