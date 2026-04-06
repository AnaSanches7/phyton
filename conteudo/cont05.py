import math
n = int(input('Digite um valor:'))
#sqrt serve para tirar raiz quadrada 
raiz = math.sqrt(n)

print('A raiz de {} é igual a: {}'.format(n,math.ceil(raiz)))
#.ceil para arredondar para cima

print('A raiz de {} é igual a: {}'.format(n,math.floor(raiz)))
#.floor para arredondar para baixo






# Funcionalidades especificas (para quando não quero importar a biblioteca): from de algo

from math import sqrt,ceil,floor

numero = int(input('Digite um numero:'))

raiz = sqrt(numero)

print('A raiz de {} é igual a: {}'.format(n,floor(raiz)))


