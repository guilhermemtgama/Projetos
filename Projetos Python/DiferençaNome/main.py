def Percentual_Nome(nome1, nome2):
    tamanho_menor_nome = min(len(nome1), len(nome2))
    num_caracteres_iguais = 0
    for i in range(tamanho_menor_nome):
        if nome1[i] == nome2[i]:
           num_caracteres_iguais += 1
           percentual_similaridade = (num_caracteres_iguais / tamanho_menor_nome) * 100
           return percentual_similaridade
#
#
nome2 = "Luna Souza Pinheiros"
nome1 = "Luna Sousa Pinheiros"
print(f'\033[32m{Percentual_Nome(nome1, nome2)}%')
