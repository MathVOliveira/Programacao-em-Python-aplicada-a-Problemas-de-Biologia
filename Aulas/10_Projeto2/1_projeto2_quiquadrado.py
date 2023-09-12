from funcao_quiquadrado import *

# Genótipo observados
pp, pq, qq = map(int, input().split())
total = pp + pq + qq

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
