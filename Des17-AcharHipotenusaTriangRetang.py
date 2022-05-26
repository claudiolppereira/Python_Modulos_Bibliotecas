import math
a = float(input('Digite o valor do cateto oposto do Triângulo Retângulo: '))
b = float(input('Digite o cateto adjascente do Triângulo Retângulo: '))
c = math.hypot(a, b)
print('Cateto Oposto: {} \nCateto Adjascente: {} \n A hipotenusa do Triângulo Retângulo é: {}'.format(a, b, c))