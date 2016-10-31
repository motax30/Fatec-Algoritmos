print("Algoritmo Cálculo Idade pela Data de Nascimento")
print("--------------------------------------------------------------------------------------------")
anoNasc = int(input("Insira seu ano de nascimento com 4(quatro) algarismos: "))
anoAtual = 2016
idade = anoAtual - anoNasc
if(idade>=16):
    if(idade>18):
        print("Você tem %d anos, você já podendo votar e também tirar sua Carteira de Habilitação"%idade)
    else:
        print("Você tem %d anos e já pode votar"%idade)
else:
    print("Você é menor de idade, você tem %d anos"%idade)