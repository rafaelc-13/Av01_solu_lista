'''Escreva um algoritmo para ler o
número total de eleitores de um
município, o número de votos brancos,
nulos e válidos. Calcular e escrever o
percentual que cada um representa em
relação ao total de eleitores.'''

eleitores = int(input("Numero total de eleitores: "))
votos_b = int(input("Numero de votos em branco: "))
votos_n = int(input("Numero de votos nulos: "))
votos_v = int(input("Numero de votos válidos: "))

p_brancos = (votos_b / eleitores) * 100
p_nulos = (votos_n / eleitores) * 100
p_valid = (votos_v / eleitores) * 100

print("A porcentagem de votos brancos é:",p_brancos,"\n"
"A porcentagem de votos nulos é:",p_nulos,"\n"
"A porcentagem de votos válidos é:",p_valid,"\n")

