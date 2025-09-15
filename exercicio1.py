texto = input("Digite seu texto aqui: ")
lista_de_palavras = texto.split()
contador_de_palavras = len(lista_de_palavras)
print(f"O seu texto tem {contador_de_palavras} palavras.")
palavra_mais_longa = ""
tamanho_maior = 0
for palavra in lista_de_palavras:
    if len(palavra) > tamanho_maior:
        tamanho_maior = len(palavra)
        palavra_mais_longa = palavra
print(f"A palavra mais longa é: '{palavra_mais_longa}'")
contagem_das_palavras = {}
for palavra in lista_de_palavras:
    palavra_limpa = palavra.lower()
    contagem_das_palavras[palavra_limpa] = contagem_das_palavras.get(palavra_limpa, 0) + 1
palavra_mais_frequente = ""
maior_contagem = 0
for palavra, contagem_atual in contagem_das_palavras.items():
    if contagem_atual > maior_contagem:
        maior_contagem = contagem_atual
        palavra_mais_frequente = palavra
print(f"A palavra que mais aparece é: '{palavra_mais_frequente}'")
