import re

# busca sofisticada por padrões
    # padrões de busca são praticamente ilimitados

frase = 'Olá, meu número de telefone é (42)0000-0000'
frase2 = 'A placa de carro que eu anotei durante o aceidente foi FRT-1998'
email = 'Entre em contato, meu email é teste@teste.com'
frase3 = 'FRT-1998 é a placa do carro'
frase4 = 'Meu número de telefone atual é (42)0000-0000. O número (56)1111-1111 é antigo'
emails = '''Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com'''

# MÉTODOS (funções)
    # search >> encontrar as posições de padrões dentro de uma string, se estes estiverem presentes
a1 = re.search('\(\d{2}\)\d{4,5}\-\d{4}', frase)
print(a1)
a2 = re.search('[A-Za-z]{3}\-\d{4}', frase2)
print(a2)
a3 = re.search('\w+@\w+\.com', email)
print(a3)
    
    # match >> encontrar se o começo de uma string é igual a um determinado padrão
b1 = re.match('[A-Za-z]{3}\-\d{4}', frase)
print(b1)
b2 = re.match('[A-Za-z]{3}\-\d{4}', frase3)
print(b2)

    # findall >> encontrar todas as substrings em uma string que correspondam a um padrão
        # substring >> pedaços de uma string
        # retorna em formato de lista o encontrado
c1 = re.findall('\(\d{2}\)\d{4,5}\-\d{4}', frase4)
print(c1)
c2 = re.findall('\w+@\w+\.\w*', emails)
print(c2)


# METACARACTERES
    # . >> qualquer caractere (exceto linha nova)

    # \w >> qualquer caractere alfanumérico

    # \W >> qualquer caractere não-alfanumérico

    # \d >> qualquer caractere que seja um dígito (0-9)

    # \D >> qualquer caractere não dígito

    # \s >> espaço em branco

    # ^ >> comaça com uma determinada letra escolhida

    # $ >> termina com uma determinada letra

    # \ >> usado antes de metacaracteres para especificar seu significado literal


# QUANTIFICADORES >> permitem determinar como e quantas vezes os metacaracteres aparecem
    # [] >> opcional entre os que estão dentro dos colchetes

    # () >> captura grupos de caracteres

    # * >> de zero a mais vezes

    # ? >> zero ou uma vez

    # + >> uma ou mais vezes

    # {m,n} >> de m a n vezes

    # | >> ou

    
