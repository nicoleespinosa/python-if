# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. 
    # - Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    # - salários até R$ 280,00 (incluindo) : aumento de 20% - feito
    # - salários entre R$ 280,00 e R$ 700,00 : aumento de 15% - feito
    # - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10% - feito
    # - salários de R$ 1500,00 em diante : aumento de 5% - feito
    # - Após o aumento ser realizado, informe na tela:
    # - o salário antes do reajuste; - feito
    # - o percentual de aumento aplicado;
    # - o valor do aumento;
    # - o novo salário, após o aumento.
    
salario = float(input('Digite o salário do colaborador: R$ '))

aumento = 0
subtracao = 0
if salario <= 280:
  aumento = salario * 1.20
  subtracao = aumento - salario
  print('\nO salário antes do reajuste era R${}, com o aumento de 20%, seu salário aumentou R${}.'
      '\nO seu novo salário é R${}'.format(salario, subtracao, aumento))

elif salario > 280 and salario <= 700:
  aumento = salario * 1.15
  subtracao = aumento - salario
  print('\nO salário antes do reajuste era R${}, com o aumento de 15%, seu salário aumentou R${}.'
      '\nO seu novo salário é R${}'.format(salario, subtracao, aumento))

elif salario > 700 and salario <= 1500:
  aumento = salario * 1.10
  subtracao = aumento - salario
  print('\nO salário antes do reajuste era R${}, com o aumento de 10%, seu salário aumentou R${}.'
      '\nO seu novo salário é R${}'.format(salario, subtracao, aumento))

elif salario > 1500:
  aumento = salario * 1.05
  subtracao = aumento - salario
  print('\nO salário antes do reajuste era R${}, com o aumento de 5%, seu salário aumentou R${}.'
      '\nO seu novo salário é R${}'.format(salario, subtracao, aumento))
      
else:
  print('\nSalário Inválido.')