print("Algoritmo Classe Eleitoral!")
idade = int(input("Informe sua idade:"))
if idade<16:
    print("Você é não votante")
elif idade<18:
    print("Seu voto é facultativo")
else:
    print("Seu voto é obrigatório")