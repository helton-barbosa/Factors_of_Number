number = int(input('Entre com um número inteiro: '))

for contador in range(1, number+1):
    if number % contador == 0:
        print(contador)
