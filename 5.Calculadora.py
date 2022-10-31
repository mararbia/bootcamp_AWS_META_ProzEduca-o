# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros 
# serão os números da operação e o terceiro será a entrada que definirá a operação a 
# ser executada. Considera a seguinte definição:
# 1 - Soma
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisão
# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def caculadora(num1, num2, operacao):
  if operacao == '+':
    print("Soma")
    res = num1 + num2
  elif operacao == '-':
    print("Subtração")
    res = num1 - num2
  elif operacao == '*':
    print("Multiplicação")
    res = num1 * num2
  elif operacao == '/':
    print("Divisão")
    res = num1 / num2
  else:
    print("Operador inválido")
    res = 0
  return res

calc = caculadora(1,1,'*')
print(calc)
