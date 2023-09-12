# For

# for dentro de um range crescente
for num in range(1,6):
    print(num)
# decrescente
for num2 in range(6, 1, -1):
    print(num2)
   
# for em uma lista
lista = [1, 2, 3, 4, 5]
for n in lista:
    print(n)
    
# Somatório
soma = 0
for n2 in range(5, 0, -1):
    soma += n2

print(soma)

# for em uma palavra
palavra = 'sorvete'
for p in palavra:
    if p == 'v':
        print(p.capitalize())
    else:
        print(p)
        
# for aninhado
for i in range(0,5):
    print(i)
    print('---')
    for j in range(0,3):
        print(j)
    print()