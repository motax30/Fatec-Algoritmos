print("ALgoritmo cálculo de Comprimento,raio e Área")
dados = [
    ["A",23],
    ["C",12],
    ["V",10],
    ["C",23],
    ["C",12],
    ["A",0],
    ["V",23],
    ["A",12],
    ["V",0]
]
PI = 3.14
for i in range(0,len(dados)):
    if dados[i][0]== "A":
        if dados[i][1]== 0:
            A = 0
        else:
            A = PI * (dados[0][1]**2)
        print("O tipo escolhido foi 'A', com raio igual a %d e valor de resultado igual a:%.2f"%(dados[i][1],A))
    elif dados[i][0]== "V":
        if dados[i][1] == 0:
            V = 0
        else:
            V = (4 * PI * (dados[0][1]**2))/3
            print("O tipo escolhido foi 'V', com raio igual a %d e valor de resultado igual a:%.2f" % (dados[i][1],V))
    elif dados[i][0]== "C":
        if dados[i][1] == 0:
            C = 0
        else:
            C = 2 * PI * dados[0][1]
            print("O tipo escolhido foi 'C', com raio igual a %d e valor de resultado igual a:%.2f" % (dados[i][1],C))





