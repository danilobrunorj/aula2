try:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print(f'Esse número {numero} é par')

    elif numero % 2 == 1:
        print(f'Esse número {numero} é ímpar')

except:
    print('Você não digitou um número')
