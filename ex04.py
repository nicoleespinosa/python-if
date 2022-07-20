# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ')

if letra == 'a' and 'e' and 'i' and 'o' and 'u':
  print('A letra {} é uma vogal.'.format(letra))
else:
  print('A letra {} é uma consoante.'.format(letra))