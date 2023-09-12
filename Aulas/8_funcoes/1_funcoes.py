# FUNCOES
# trechos de programa que recebem um determinado nome e podem ser chamados várias vezes durante a execução
# principais vantagens:
    # reutilização de código
    # modularidade e facilidade de manutenção do sistema
    
# 1 - Função sem parâmetro e sem retorno
def mensagem():
    print('Mensagem teste')
    
mensagem()

# 2 - Função com passagem de parâmetro
    # o parâmetro é passado dentro dos () da função, mas precisa ser definido o parâmentro antes
def mensagem2(texto):
    print(texto)

    # serve para qualquer tipo de dado >>> str, float, int...
mensagem2('Mensagem teste 2')
mensagem2(12)
lista = ['a', 'b', 'c']
mensagem2(lista[1])

    # pode ser mais de um parâmetro por função
def soma(a, b):
    print(a + b)
    
soma(2, 4)

# 3 - Função com passagem de parâmentros e retorno
    # muito utilizado quando se quer atribuir o valor de uma função para uma var
def subtração(a, b):
    return a - b

    # não é mostrado o resultado
subtração(3, 2)
    # ao ser atribuída, basta imprimir a var
sub = subtração(3, 2)
print(sub)

    # podemos definir um valor fixo para o parâmetro, ou passar ao chamar a função
    # também podemos colocar uma descrição na função, podendo ser acessada com o comando help()
def calculo_energia_potencial_gravitacional(m, h, g = 10):
    '''
    Calcula a energia potencial gravitacional
    Argumentos obrigatório:
        m = massa, entrada como uma variável float
        h = altura, entrada como uma variável float
    Argumento opcional:
        g = aceleração gravitacional, com valor default de 10
    '''
    e = g * m * h
    return e

epg = calculo_energia_potencial_gravitacional(30, 12)
print(epg)
epg2 = calculo_energia_potencial_gravitacional(30, 12, 9.8)
print(epg2)

help(calculo_energia_potencial_gravitacional)
help(print)