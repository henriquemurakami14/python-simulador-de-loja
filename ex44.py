print("{:=^40}".format(' LOJAS AMERICANAS '))
preco_compra = float(input("Digite o valor da compra: R$"))
avista_dinheiro = preco_compra * 0.90
avista_cartao = preco_compra * 0.95
parcela2x_cartao = preco_compra
parcela3x_cartao = preco_compra * 1.20
print("Selecione a forma de pagamento:\n[1] a vista\n[2] a vista cartao\n[3] 2x no cartao\n[4] 3x ou mais cartao")
forma_pagamento = int(input("Digite a sua opcão: "))
print(" ")
if forma_pagamento == 1:
    print("Comprando a vista com dinheiro. Você ganha um desconto de 10%.")
    print("Valor da compra R${:.2f}".format(avista_dinheiro))
elif forma_pagamento == 2:
    print("Comprando a vista com o cartao. Você ganha um desconto de 5%.")
    print("Valor da compra R${:.2f}".format(avista_cartao))
elif forma_pagamento == 3:
    print("Valor da compra é de R${:.2f}".format(parcela2x_cartao))
    print("Cada parcela será de {:.2f}".format(parcela2x_cartao/2))
elif forma_pagamento == 4:
    numeros_parcelas = int(input("Numero de parcelas: "))
    print("Parcelando {} vezes cada parcela ficara R${:.2f}".format(numeros_parcelas, parcela3x_cartao/numeros_parcelas))
    print("Valor total da compra é de R${:.2f}".format(parcela3x_cartao))
else:
    print("INVALIDO. Pressione novamente a forma de pagamento")
print("Tenha um otimo dia, volte sempre!!")
