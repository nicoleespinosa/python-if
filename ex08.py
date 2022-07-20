# Faça um Programa que leia três números e mostre-os em ordem decrescente.
x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
z = float(input('Digite o terceiro número: '))

lista = [x, y, z]
lista.sort(reverse=True)
print(lista)