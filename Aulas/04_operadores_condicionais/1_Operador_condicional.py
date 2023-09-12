# OPERADOR CONDICIONAL

# IF: só inicia se a condição for True
if 5 > 3:
    print('5 é maior que 3')
    
# ELSE: usado quando nenhuma condição é atendida em IF
if 5 > 6:
    print('5 é maior que 6')
else:
    print('5 não é maior que 6')
    
# ANINHAMENTO
n = 5
if n == 4:
    print('n é igual a 4')
else:
    if n == 3:
        print('é igual a 3')
    else:
        print('n não é igual a 3 ou 4')
        
# pode-se usar operadores lógicos dentro dos condicionais
x = 2
y = 4
if (x > 1) and (y % 2 == 0):
    print('x é maior que 1 e y é par')
else:
    print('nenhuma das condições foram satisfeitas')