import random
nome = input("Digite seu nome: ")
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
tamanho_nome = len(nome)
tamanho_total = 20
tamanho_ate_agora = 0
senha_aleatoria = ""
while True:
    if tamanho_ate_agora < (tamanho_total - tamanho_nome) // 2:
        caractere_sorteado = random.choice(caracteres)
        senha_aleatoria = senha_aleatoria + caractere_sorteado
        tamanho_ate_agora = tamanho_ate_agora + 1
    else:
       break
senha_aleatoria = senha_aleatoria + nome
tamanho_ate_agora = tamanho_ate_agora + tamanho_nome
while True:
    if tamanho_ate_agora < tamanho_total:
        caractere_sorteado = random.choice(caracteres)
        senha_aleatoria = senha_aleatoria + caractere_sorteado
        tamanho_ate_agora = tamanho_ate_agora + 1
    else:
        break
print("Sua nova senha aleatória com seu nome é:")
print(senha_aleatoria)
