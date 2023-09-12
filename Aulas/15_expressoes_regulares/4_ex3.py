# detectando doença genética

import re

seqRNA = input('Insira a sequência de RNA: ')

if (re.search('(CAA|CAG){35,}', seqRNA)) != None:
    print("O padrão foi encontrado")
else:
    print("O padrão não foi encontrado")
