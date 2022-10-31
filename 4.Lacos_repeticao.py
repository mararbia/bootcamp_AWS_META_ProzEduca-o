# Aprender a executar laços de repetição

# Precisamos imprimir um número para cada andar de um hotel de 20 andares. 
# Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar. 
# Escreva um código que imprima todos os números exceto o número 13. 
# Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez 
# usando os outros dois tipos de laços de repetição aprendidos. 
# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

# Utilizando o For
# contador = 20

# for i in range(contador, 0, -1):
#   if(i != 13):
#     print(i)

# Utilizando o for com o "continue", "break" e "decremento"
# contador = 21

# for i in range(20): 
#   contador = contador - 1 
#   if contador == 13:
#     continue  
#   if contador == 21:
#     break  
#   print(contador)

# Utilizando o While
# contador = 20

# while contador > 0:
#   if contador != 13:
#     print(contador)
#   contador = contador - 1
