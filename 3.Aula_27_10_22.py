# 1 - Inserir estaticamente dua bebida favorita, o seu valor e se é ou não alcóolica
# e exibir sua resposta para o usuario

# bebida_favorita = "Água com Gás"
# preco = 2.50
# alcoolica = False

# print(bebida_favorita, preco, alcoolica)

# 2 - Montar seu almoco favorito e os seguintes valores:
# preço do almoço, preço da bebida, seu orçamento, calcular o total e a diferença que será
# o troco. Após isso, exibir para o usuário na tela.

almoco_favorito = "Arroz com Lentilha (Mjadra) + Tabule + Alface + Bife + Batata Frita"
bebida_favorita = "Água com Gás"
preco_almoco = 20.00
preco_bebida = 2.50
orcamento = 35.00
total = preco_almoco + preco_bebida

diferenca = orcamento - total

print("Almoço Favorito: " + almoco_favorito + "\nBebida Favorita: " + bebida_favorita)
print("Preço do almoço com bebida: R$", total)
print("Orçamento: R$", orcamento, "\nTroco: R$", diferenca)

# Curiosidade
# Outro jeito de motsrar a diferença com o operador resto
# difTotal = diferenca % total 
# print(difTotal)