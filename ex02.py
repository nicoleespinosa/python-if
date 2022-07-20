# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input('Digite um valor: '))
if valor < 0:
  print('O valor {} é negativo.'.format(valor))
elif valor > 0:
  print('O valor {} é positivo.'.format(valor))
else:
  print('O valor é inválido')