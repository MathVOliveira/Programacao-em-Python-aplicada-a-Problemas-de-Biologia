# lembrar que funções recebem parâmetros, que também podem ser listas
def qui_quadrado(x, y):
    soma = 0
    for observado, esperado in zip(x, y):
        soma += (observado-esperado)**2/esperado
        
    return soma