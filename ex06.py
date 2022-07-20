# Faça um Programa que leia três números e mostre o maior deles.
x = float(input('Digite o primeiro número: '))
y = float(input('Digite o seguno número: '))
z = float(input('Digite o terceiro número: '))

if x > y and x > z:
  print('O maior valor é {}'.format(x))
elif y > x and y > z:
  print('O maior valor é {}'.format(y))
elif z > x and z > y:
  print('O maior valor é {}'.format(z))
else:
  print('Valor inválido')