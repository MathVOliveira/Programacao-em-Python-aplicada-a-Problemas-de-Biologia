# Encontrando ORF's

import re

seqRNA1 = 'GGCGGGCACCGACGGAUGGCAACGGUUUAUUUUCCUUUAUAGAGGGGCCCCCUUAC'
seqRNA2 = 'GGCGGGCACCGACGGAUGGCAACGGUUUAUUUUCCUUUAUAAAGGGGCCCCCUUAC'
seqRNA3 = 'GGCGGGCACCGACGGAUGGCAACGGUUUAUUUUCCUUUAUCAAGGGGCCCCCUUAC'


# forma que eu fiz
print(re.search('AUG\w*UAG|AUG\w*UAA|AUG\w*UGA', seqRNA1))
# nesse segundo exemplo, a (...) indica que tem caracteres no meio, sempre múltiplo do tanto de ponto
print(re.search('AUG(...)+U(AG|GA|AA)', seqRNA2))
# importante saber que o (...) pega qualquer tipo de caractere
print(re.search('AUG(...)+U(AG|GA|AA)', seqRNA3))

def identifica_orf(seq):
    if (re.search('AUG\w*UAG|AUG\w*UAA|AUG\w*UGA', seq)) != None:
        return True
    else:
        return False
    
print(identifica_orf(seqRNA1))
print(identifica_orf(seqRNA3))
