import math
num = int(input('Digite qual é o ângulo: '))

angulo = math.radians(num)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('Dados para o angulo: {:.0f}'.format(num))
print('O Seno é: {:.4f} \nO Cosseno é: {:.4f} \nA Tangente é: {:.4f}'.format(seno, cosseno, tangente))