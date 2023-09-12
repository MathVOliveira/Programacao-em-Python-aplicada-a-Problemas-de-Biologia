# math >>> https://docs.python.org/3/library/math.html
import math
    # funções da biblioteca (alguns exemplos)
print(math.sqrt(9))
print(math.sin(45))
print(math.cos(45))
print(math.log(1000,10))
    # constantes da biblioteca (alguns exemplos)
print(math.e)
print(math.pi)


# datetime >>> https://docs.python.org/3/library/datetime.html
import datetime
    # saber as funções da biblioteca
print(dir(datetime))
    # funções
print(datetime.date.today())
print(datetime.datetime.now())
data = datetime.date(2020, 7, 10)
print(data)
print(data.day, data.month, data.year)
horario = datetime.datetime(2020, 7, 10, 7, 30, 0)
print(horario)
print(horario.hour, horario.minute, horario.second)


# random >>> https://docs.python.org/3/library/random.html
import random
    # gera um número entre 0 e 1
print(random.random()) 
    # gera em uma faixa específica
print(random.randint(1, 5))
    # gera números em um intervalo de salto
print(random.randrange(0,10,2))
print(random.randrange(0,10,3))
    # 'sorteio'
x = ['k', 'd', 13, '34-j', 'X']
print(x)
print(random.choice(x))


# time >>> https://docs.python.org/3/library/time.html
import time as tm
    # tempo em segundos
print(tm.time())
    # vendo quanto tempo levou para rodar um código
antes = tm.time()
lista = []

for i in range(0, 100000):
    lista.append(i)

depois = tm.time()
intervalo = depois - antes
print(f'tempo: {intervalo} segundos')

    # 'esperar um tempo'
print('finalizando...')
tm.sleep(2)
print('...')
tm.sleep(2)
print('até a próxima')








