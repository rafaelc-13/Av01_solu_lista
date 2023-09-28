'''Faça um algoritmo que leia a idade de
uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa
apenas em dias. Considerar ano com 365
dias e mês com 30 dias.'''

a = int(input("Quantos anos você tem: "))
m = int(input("Quantos meses a mais: "))
d = int(input("Quantos dias a mais: "))
idade = a*365+m*30+d

print("Sua idade, em dias, é: ",idade)
