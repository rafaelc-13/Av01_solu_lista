'''Crie um código que leia a idade de
uma pessoa e diga em qual ano ela
nasceu'''

n = int(input("Digite sua idade: "))
mes_idade = int(input('Em qu mês voce nasceu (1-12)? '))
mes_atual = int(input('Em qu mês do ano estamos (1-12)? '))
IDADE = 2023 - n

if mes_idade >= mes_atual:
    IDADE -=1

print(f'Você nasceu em {IDADE}.')

