# Verificando os tipos de dados

# 1 ---------------------------------------

# numero_inteiro = 5
# numero_float = 5.7
# texto = "Este é um texto"
# booleano = False

# print("Este é um tipo")
# print(type(numero_inteiro))
# print("Este é um tipo")
# print(type(numero_float))
# print("Este é um tipo")
# print(type(texto))
# print("Este é um tipo")
# print(type(booleano))

# print("Esse é o conteúdo da variável")
# print(numero_inteiro)

# 2 ---------------------------------------

# variavel = 5
# print("Primeiro tipo")
# print(type(variavel))
# variavel = "texto"
# print("Segundo tipo")
# print(type(variavel))

# 3 ---------------------------------------
# Definindo uma variável

# var = 6
# print("Esta é a primeira aparição da variável")
# print(var)
# print("Esta é a segunda aparição da variável")
# print(var)
# print("Esta é a terceira aparição da variável")
# print(var)
# print("Esta é a quarta aparição da variável")
# print(var)
# print("E você só definiu o valor uma única vez")

# 4 ---------------------------------------
# Declarando uma variável com tipo definido

# texto = "10"
# num = int(texto)

# print(texto + str(10))
# print(num + 10)

# 5 ---------------------------------------
# Desenvolva um programa que utiliza o nome de um aluno, duas notas e a 
# quantidade de faltas que ele teve. Conclua se o aluno está aprovado ou 
# reprovado de acordo com as especificações:

# Se a média do aluno for menor que sete, o sistema deve informar o nome 
# do aluno e que ele está reprovado;
# Se o aluno possuir mais de três faltas, o sistema deve informar o nome 
# do aluno e que ele está reprovado;
# Se a média do aluno for maior ou igual a sete, o sistema deve informar 
# o nome do aluno e que ele está aprovado.
# No sistema, todos os valores devem estar armazenados em variáveis.

# nomeAluno = "Mara"
# nota1 = 7
# nota2 = 7
# faltas = 3

# media = (nota1 + nota2) / 2

# if media < 7 or faltas > 3:
#     print("Reprovado")
# elif media >= 7:
#    print("Aprovado")

# 6 ---------------------------------------
# Iniciando com funções

# def ant_e_suc(num):
#   ant = num - 1
#   suc = num + 1
#   return ant, suc

# antecessor, sucessor = ant_e_suc(5)
# print(antecessor)
# print(sucessor)


# 7 ---------------------------------------
# Problema: João precisa calcular seu Índice de Massa Corporal (IMC) 
# para avaliar seu peso ideal. 
# Sabendo que a fórmula para calcular o IMC é: peso ÷ altura², 
# crie um programa que calcule e informe a classificação do IMC.

# def calc_imc(peso, altura):
#   imc = peso / (altura * altura)
#   return imc

# imc = calc_imc(70, 1.55)

# if imc <= 18.5:
#   print("Abaixo do peso")
# elif imc >= 18.6 and imc <= 24.9:
#   print("Peso ideal")
# elif imc >= 25.0 and imc <= 29.9:
#   print("Levemente acima do peso")
# elif imc >= 30.0 and imc <= 39.9:
#   print("Obesidade grau II - Severa")
# else:
#   print("Obesidade grau III - Mórbida")

# 8 ---------------------------------------
# Usando o range

# def aprovacao(num_lim, incre):
#   contador = 0
#   for i in range(0, num_lim, incre):
#     contador = contador + 1
#   return contador

# aprov = aprovacao(20, 1)
# print(aprov)

# 9 ---------------------------------------
# Usando o try e except
# Problema: Desenvolva um programa que só deve aceitar números pares. Siga as seguintes instruções:
# caso um número ímpar seja digitado, informe ao usuário que ele digitou um valor ímpar e peça novamente por um número par;
# caso uma letra seja digitada, informe ao usuário que ele digitou um caractere inválido e peça novamente por um número par.

try:
  print("Digite um número par: ")
  numPar = float(input())

  if numPar % 2 == 0:
    print("Muito bem!!! O número digitado", numPar, "é par!")
  else:
    print("Número ímpar, favor digitar um número par")   
except:
  print("Caractere inválido, favor digitar um número par")