def limpar_texto(texto):
    texto = texto.lower()
    caracteres = ",.!|?;:\"'()[]{}"
    for char in caracteres:
        texto = texto.replace(char, "")
    return texto

def conta_palavras(frase):
    frase = limpar_texto(frase)
    palavras = frase.split()
    return len(palavras)