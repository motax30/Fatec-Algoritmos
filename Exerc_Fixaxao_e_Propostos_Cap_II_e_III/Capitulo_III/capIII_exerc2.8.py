print("Algoritmo Condição de Pagamento")
print("--------------------------------------------------------------------------------------------")
precoNormal = float(input("Informe o preço normal de etiqueta do produto"))
cond = input("Informe a condição de pagamento, conforme a tabela abaixo:\n"
             "(1)À vista em dinheiro ou cheque, recebe 10% de desconto\n"
             "(2)À vista no cartão de crédito, recebe 5% de desconto\n"
             "(3)Em duas vezes, preço normal de etiqueta sem juros\n"
             "(4)Em três vezes, preço normal de etiqueta maisd juros de 10%")
if(cond=="1"):
    precoFinal = precoNormal-(precoNormal*0.10)
elif(cond=="2"):
    precoFinal = precoNormal-(precoNormal*0.05)
elif(cond=="3"):
    precoFinal =
elif(cond=="4"):
    precoFinal =
