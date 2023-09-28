'''. Escreva um algoritmo para ler dois
valores (considere que não serão lidos
valores iguais) e escrevê-los em ordem
crescente'''

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
if n1 > n2:
    print(f"{n1} é maior que {n2}.")
else:
    print(f"{n2} é maior que {n1}.")

