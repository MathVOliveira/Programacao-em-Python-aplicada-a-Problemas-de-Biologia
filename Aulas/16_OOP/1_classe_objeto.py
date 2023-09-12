# Classe (molde)

# agrupamento de objetos similares que apresentam os mesmos:
    # atributos (características) e métodos (ações)
# Molde de bonecos de gesso
    # difine o formato e tamanho
    # o molde é sempre o mesmo, porém os objetos podem ter características variadas, respeitando
    # a estrutura básica do molde


    
# criando a classe
class Triangulo:
    # função para atribuição das caracteríscticas do objeto que será criado
    def __init__(self, lado1, lado2, lado3, base, altura):
        # criando as características
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2

    def tipo(self):
        if self.lado1 > self.lado2 + self.lado3:
            return 'não é um triângulo'
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado2 == self.lado3:
            return 'triângulo isósceles' # errado
        else:
            return 'outro tipo de triângulo'
        
        

t1 = Triangulo(2, 1, 3, 4, 3)
print(t1.lado1, t1.lado2, t1.lado3, t1.base, t1.altura)

t2 = Triangulo(8, 8, 8, 16, 9)
print(t2.lado1, t2.lado2, t2.lado3, t2.base, t2.altura)

print(t1.area())
print(t2.area())

print(t1.tipo())
print(t2.tipo())