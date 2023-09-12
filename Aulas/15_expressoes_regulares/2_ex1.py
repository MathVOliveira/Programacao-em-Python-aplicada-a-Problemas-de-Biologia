# extração de nomes científicos no texto

import re

texto = '''Das espécies mais próximas de H. sapiens atualmente vivas,
podemos citar P. troglodytes e P. paniscus, os quais assim apresentam diferenças
notáveis nos mais diversos níveis'''

print(texto)

nomes_científicos = re.findall('\w+\.\s\w*', texto)
print(nomes_científicos)
print(type(nomes_científicos))