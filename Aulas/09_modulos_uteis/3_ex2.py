# Cálculo: população final

import math

def calculo_pop_final():
    e = math.e
    n0 = float(input("Tamanho da população inicial: "))
    r = float(input("Taxa de crescimento: "))
    t = float(input("tempo de crescimento em dias: "))
    # n0, r, t = map(float, input().split())
    nt = n0*(e**(r*t))
    
    return int(nt)

populacao_final = calculo_pop_final()
print(populacao_final)

print(f'População inicial de 1000 indivíduos, população final de {populacao_final}.')