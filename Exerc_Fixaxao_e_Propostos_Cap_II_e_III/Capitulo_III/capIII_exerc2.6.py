print("Algoritmo Classificação de Produtos")
print("--------------------------------------------------------------------------------------------")
print("LIsta de Códigos:\n (1)Alimento não-perecível\n(2,3 ou 4)Alimento perecível\n(5 ou 6)Vestuário\n (7)Higiene pessoal, \n(8 até 15)Limpeza e Utensílios Domésticos\n")
codProduto = int(input("Digite um código para ver sua classificação, conforme mostrado acima: "))
if(codProduto==1):
    print("O produto de código(%d) tem a seguinte classificação: Alimento não-perecível"%codProduto)
elif(codProduto<=4):
    print("O produto de código(%d) tem a seguinte classificação: Alimento perecível"%codProduto)
elif(codProduto<=6):
    print("O produto de código(%d) tem a seguinte classificação: Vestuário"%codProduto)
elif(codProduto==7):
    print("O produto de código(%d) tem a seguinte classificação: Higiene pessoal"%codProduto)
elif(codProduto<=15):
    print("O produto de código(%d) tem a seguinte classificação: Limpeza e Utensílios Domésticos"%codProduto)
else:
    print("Número inválido")
