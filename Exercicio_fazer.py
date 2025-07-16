'''

# exercicio 1
print("alo mundo")

# exercicio 2
n1 = input ("Digite um número: ")
print ("Você digitou o número:", n1)

# exercicio 3

primeiro = int( input (" Digite o primeiro número:  "))
segundo = int (input (" Digite o segundo número:  "))
total = (primeiro + segundo)
print  ("A soma é igual a: ",total)

#exercicio 4
primeira_nota = int( input (" Digite o primeiro número:  "))
segunda_nota = int (input (" Digite o segundo número:  "))
terceiraa_nota = int( input (" Digite o terceiro número:  "))
quarta_nota = int (input (" Digite o quarto número:  "))

media = (primeira_nota + segunda_nota + terceiraa_nota + quarta_nota)/4
print(media)



#exercicio 5

metros = int (input ("Digite quantos Metros deseja converter para cm:  "))
centimetros = (metros) * 100 
print (centimetros,"cm")


#exercicio 6
area = int (input ("  Digite a área do círculo:  "))
raio = (area/3.14159)**0.5
print("O raio é,", raio)

#exercicio7
area = int ( input("Para saber a área do quadrado, digite o tamanho do lado:  "))
area_quadrado = area**2
print (area_quadrado)


#exercicio 8

ganho_por_hora = float ( input( "digite quanto você ganha por hora: "))
horas_trabalhadas_por_mes = float ( input( "digite quantas horas você trabalha por mês: "))
salario = (ganho_por_hora * horas_trabalhadas_por_mes)
print ("seu salário é:" ,salario)


#exercicio9

grau_Farenheit = float(input("digite o grau em Farenheit: "))
graus_celcius = (5 * (grau_Farenheit-32) / 9)
print ("Graus Celcius é: ", graus_celcius)

'''
#exercicio 10

graus_celcius= float(input("digite o grau em celcius: "))
grau_Farenheit = (graus_celcius *1.8)+32
print ("Graus Farenheit é: ", grau_Farenheit)



