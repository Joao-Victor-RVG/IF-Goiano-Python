import math


class Circulo:
    def escreva(self):
        self.raio = float(input())
    
    def area(self):
        area = (self.raio ** 2) * 3.14
        print(f'Área do círculo: {area:.2f}')
    
    def perimetro(self):
        perimetro = 2 * 3.14 * self.raio
        print(f'Perímetro do círculo: {perimetro:.2f}')

x = Circulo()
x.escreva()
x.area()
x.perimetro()
