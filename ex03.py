# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sx = input('Qual o seu sexo? ')

if sx == 'f':
  print('Sexo F-Feminino')
elif sx == 'm':
  print('Sexo M-Masculino')
else:
  print('Sexo inválido')
