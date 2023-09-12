# While

numero = 1
while numero < 6:
    print(numero)
    numero += 1
    
n = 5
while n > 0:
    print(n)
    n -= 1
    
num = 1
soma = 0
while num < 6:
    soma += num
    num += 1
    
print(soma)

# atenção a var n2, precisa ser negativa ou maior que 10 para que entre no loop
n2 = -1
while n2 < 1 or n2 > 10:
    n2 = int(input("Digite um número de 1 a 10: "))
    