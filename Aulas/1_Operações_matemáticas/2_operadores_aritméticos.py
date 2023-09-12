import math # tentar ver pq não deu certo

# Operações matemáticas
a = 5
b = 3
print(a, b)
    
print(a + b) # soma
print(a - b) # subtração
print(a * b) # multiplicação
print(a / b) # divisão
print(a % b) # resto da divisão
print(a ** b) # elevado
# import (não está indo, não sei pq)
math.sqrt(81) # raiz quadrada (não usar assim pelo jeito)
print(math.sqrt(81)) # assim deu certo

# Arredondamento
casos_doenca = 134
num_habitantes = 34432
casos_por_habitantes = casos_doenca / num_habitantes

# ambos os comandos abaixo arredondam o valor
print(f'{casos_por_habitantes:.4f}') # :.nf para escolher o número de casas após a vírgula
print(round(casos_por_habitantes, 6)) # também pode ser usado assim