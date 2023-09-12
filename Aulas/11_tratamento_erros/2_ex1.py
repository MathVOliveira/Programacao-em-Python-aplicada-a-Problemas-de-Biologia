# lembrar que funções recebem parâmetros, que também podem ser listas
def qui_quadrado(x, y):
    soma = 0
    for observado, esperado in zip(x, y):
        soma += (observado-esperado)**2/esperado
        
    return soma

while True:
    try:
        pp, pq, qq = map(int, input().split())
    except ValueError:
        print("algum valor está inválido, tente novamente.")
    else:
        print("calculando")
        total = pp + pq + qq
        break

# frequência
freq_alelo_P = (2*pp+pq)/(2*total)
freq_alelo_Q = (2*qq+pq)/(2*total)

# esperados
pp_esperado = (freq_alelo_P**2)*total
pq_esperado = (2*freq_alelo_P*freq_alelo_Q)*total
qq_esperado = (freq_alelo_Q**2)*total
total_esperado = pp_esperado + pq_esperado + qq_esperado

# coleções
observados = (pp, pq, qq)
esperados = (pp_esperado, pq_esperado, qq_esperado)

print(qui_quadrado(observados, esperados))