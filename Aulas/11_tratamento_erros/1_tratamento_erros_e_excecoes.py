# Tratamento de erros

# tipos de erros
    # NameError - vavriável não foi definida
    # TypeError - tipos de dados incompatíveis
    # RuntimeError - erro de execução
    # SyntaxError - sintaxe digitada é inválida e não reconhecida pelo interpretador
    # ZeroDivisionError - divisão por zero
    # IndexError - índice fora da coleção

# tratamento de erros
while True:
    try:
        n = int(input('Digite um número inteiro: '))
    except:
        print("valor inválido")
    else:
        print(f'valor correto: {n}')
        break

while True:
    try:
        p = int(input("outro número: "))
    except ValueError:
        print("valor inválido")
    except KeyboardInterrupt:
        print("interrompendo")
        break
    else:
        print(f'o número digitado foi {p}')
        break
    