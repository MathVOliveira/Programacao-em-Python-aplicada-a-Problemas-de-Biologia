glicina = 0
aspartato = 0
leucina = 0

with open("13_manipulacao_arq_texto/Nova pasta/1trl.pdb", "r") as protein:
    for linha in protein:
        if 'GLY' in linha:
            glicina += 1
        elif 'ASP' in linha:
            aspartato += 1
        elif 'LEU' in linha:
            leucina += 1
            
print(f'glicina: {glicina};\naspartato: {aspartato};\nleucina: {leucina}.')