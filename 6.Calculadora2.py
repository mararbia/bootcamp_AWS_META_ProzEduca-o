# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
# O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
# No início, o programa mostrará a seguinte lista de operações:
# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair
# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
# o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.
# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, 
# um de cada. Depois precisa executar a operação e mostrar o resultado na tela. 
# Quando o usuário escolher a opção “Sair”, o sistema irá parar.
# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.

def somar(num1, num2):
  soma = num1 + num2
  return soma

def subtrair(num1, num2):
  sub = num1 - num2
  return sub

def multiplicar(num1, num2):
  mult = num1 * num2
  return mult

def dividir(num1, num2):
  div = num1 / num2
  return div

print("Escolha a operação metemática: ")
print("0 - Sair \n1 - Somar \n2 - Subtrair \n3 - Multiplicar \n4 - Dividir")
opcao = int(input())

while opcao != 0:    
    
    while opcao != 0 and opcao != 1 and opcao!= 2 and opcao != 3 and opcao != 4:
        print("Valor inválido! Tente novamente")
        opcao = int(input())
    
    print("Digite um número: ")
    num1 = float(input())
    print("Digite outro número: ")
    num2 = float(input())

    if opcao == 1:
        operacao = "soma"
        res = somar(num1, num2)1
    elif opcao == 2:
        operacao = "subtração"
        res = subtrair(num1, num2)
    elif opcao == 3:
        operacao = "multiplicação"
        res = multiplicar(num1, num2)
    elif opcao == 4:
        operacao = "divisão"
        res = dividir(num1, num2)
        
    print("O resultado da " + operacao + " é: ", res)

    print("Escolha a operação metemática: ")
    print("0 - Sair \n1 - Somar \n2 - Subtrair \n3 - Multiplicar \n4 - Dividir")
    opcao = int(input())