minha_lista_de_numeros = []

minha_lista_de_numeros.append(int(input("Digite o 1º número: ")))
minha_lista_de_numeros.append(int(input("Digite o 2º número: ")))
minha_lista_de_numeros.append(int(input("Digite o 3º número: ")))
minha_lista_de_numeros.append(int(input("Digite o 4º número: ")))
minha_lista_de_numeros.append(int(input("Digite o 5º número: ")))
minha_lista_de_numeros.append(int(input("Digite o 6º número: ")))
minha_lista_de_numeros.append(int(input("Digite o 7º número: ")))
minha_lista_de_numeros.append(int(input("Digite o 8º número: ")))
minha_lista_de_numeros.append(int(input("Digite o 9º número: ")))
minha_lista_de_numeros.append(int(input("Digite o 10º número: ")))
print("Lista original:")
print(minha_lista_de_numeros)
lista_ordenada = []
for numero in minha_lista_de_numeros:
    lista_ordenada.append(numero)
for i in range(len(lista_ordenada)):
    for j in range(len(lista_ordenada)):
        if lista_ordenada[i] < lista_ordenada[j]:
            numero_temporario = lista_ordenada[i]
            lista_ordenada[i] = lista_ordenada[j]
            lista_ordenada[j] = numero_temporario
print("Lista ordenada crescente:")
print(lista_ordenada)
lista_sem_repetidos = []
for numero in lista_ordenada:
    if numero not in lista_sem_repetidos:
        lista_sem_repetidos.append(numero)
    else:
        passprint("Lista sem números repetidos:")
print(lista_sem_repetidos)
