# Manipulação de Strings

n1 = 10
n2 = 5
print(f'{n1}/{n2} = {n1/n2}') # forma de usar a variável dentro da str

# variável para testes, espaços em branco também contam como caracteres, e entram em contagens
a = 'casaco'
b = 'Matheus Viana de Oliveira'
c = 'matheus viana de oliveira'
d = ' MATHEUS VIANA DE OLIVEIRA '

# primeira letra maiúscula, porém só a primeira letra de toda a str
print(a.capitalize()) 

# tudo maiúsculo
print(a.upper()) 

# tudo minúsculo
print(d.lower()) 

# busca o que foi digitado primeiro e troca pelo segundo
print(a.replace('a', 'o')) 

# procura na string o valor digitado e mostra a posição encontrada, mas só do primeiro
print(c.find('a')) 
    # retorna -1, ou seja, não foi encontrado
print(a.find('d')) 

# retorna o comprimento da str, nesse caso, a contagem começa a partir de 1
print(len(d)) 

# retira espaços, mas só os que vierem antes e depois do que está escrito, não os do meio
print(d.strip()) 
