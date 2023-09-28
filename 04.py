'''Crie um algoritmo que receba 3
números e informe qual o maior entre
eles'''

''''x=1
n1 = int(input(f"{x}º Valor: "))
n2 = int(input(f"{x+1}º Valor: "))
n3 = int(input(f"{x+2}º Valor: "))

if n1>n2:
    if n1>n3:
        print("O maior valor é o:",n1)
    else:
        print("O maior valor é o:",n3)
elif n2>n1 :
    if n2>n3:
        print("O maior valor é o:",n2)
    else:
        print("O maior valor é o:",n3)''''


n1 = float(input('Digite 1ª Número: '))
n2 = float(input('Digite 2ª Número: '))
n3 = float(input('Digite 3ª Número: '))

if n1 > n2 > n3:  #considerar fluxo do programa, como ele compara primeiro, a  primeira condição
    print(f'O maior número foi: {n1}.')
elif n2 > n3:
    print(f'O maior número foi o {n2}.')
else:
    print(f'O maior número foi: {n3}')
