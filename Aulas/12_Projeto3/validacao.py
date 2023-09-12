def valida(pergunta):
    while True:
        try:
            num = int(input(f'{pergunta}'))
        except ValueError:
            print("Valor inválido, tente novamente")
        else:
            if num == 1 or num == 2:
                break
            else:
                print("Digite uma das alternativas.")
    return num
            
