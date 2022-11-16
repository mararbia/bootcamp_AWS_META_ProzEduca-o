
# Desenvolva um programa que recebe do usuário nome completo e 
# ano de nascimento que seja entre 1922 e 2021. A partir dessas 
# informações, o sistema mostrará o nome do usuário e a idade 
# que completou, ou completará, no ano atual (2022).
# Caso o usuário não digite um número ou apareça um inválido no 
# campo do ano, o sistema informará o erro e continuará perguntando 
# até que um valor correto seja preenchido.

condicao = False

while (condicao == False): 

  try:
    print("Digite seu nome: ")
    nome = str(input())
    print("Digite o ano de seu nascimento: ")
    ano = int(input())

    if ano >= 1922 and ano <= 2021:
      idade = 2022 - ano
      
      print(nome + " a sua idade em 2022 é:", idade)
      condicao = True
  except:
    print("Favor inserir os dados corretos")
