# CRESCIMENTO BACTERIANO

pop_inicial = 500
horas = 0

while pop_inicial < 100000:
    pop_inicial = int(pop_inicial*2.5)
    horas += 3
    print(pop_inicial)
    
print(f"A população levará cerca de {horas} horas para chegar em 100.000 indivíduos")