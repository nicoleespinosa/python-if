# Faça um Programa que peça dois números e imprima o maior deles.

print('Bem-vindo(a)! \nVamos calcular pra você o maior e menor número.')

x = float(input('\nDigite o primeiro número: '))
y = float(input('Digite o segundo número: '))

if x > y:
  print('O número {} é maior que {}'.format(x, y))
elif y > x:
  print('O número {} é maior que {}'.format(y, x))
elif y == x:
  print('Os números {} e {} possuem o mesmo valor'.format(x, y))
else:
  print('Valores inválidos')