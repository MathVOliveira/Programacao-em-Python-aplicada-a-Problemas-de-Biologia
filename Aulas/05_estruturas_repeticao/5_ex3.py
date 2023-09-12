# FASES DO CRESCIMENTO BACTERIANO

bacterias = int(input("tamanho da população em Fase-lag (15 horas): "))
hora = 0

while bacterias > 0:
    
    if hora <= 15:
        bacterias = bacterias
    elif hora <= 25:
        bacterias = bacterias*2.5
    elif hora <= 30:
        bacterias = bacterias
    elif hora > 30:
        # int pois não existe 'meia vida', ou está vivo, ou morto
        bacterias = int(bacterias*0.5)
    
    hora += 1
    print(f'População de bactérias em {hora} hora(s): {bacterias}')
    
print(f'Após {hora} horas, a população chegou a 0 indivíduos')
    
    