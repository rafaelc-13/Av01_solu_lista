#Crie um código que leia um número
#diferente de zero e diga se este número
#é positivo ou negativo

n = int(input("Digite um valor diferente de zero:"))

while n == 0:
    n = int(input("Diferente de zero! \n"
                  "Tente novamente: "))
if n>0:
    print("Esse valor é positivo.")
else:
    print("Esse valor é negativo")

