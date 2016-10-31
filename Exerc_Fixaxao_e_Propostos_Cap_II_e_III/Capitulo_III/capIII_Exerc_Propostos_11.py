print("Algoritmo Classificação Olímpica!")
x=0
paises = []
while x<3:
    tmp = []
    tmp.append(input("Informe o %dºpaís:"%(x+1)))
    qtdOuro = int(input("Informe o número de medalhas de ouro do %dº país:"%(x+1)))
    qtdPrata = int(input("Informe o número de medalhas de prata do %dº país:" %(x+1)))
    qtdBronze = int(input("Informe o número de medalhas de bronze do %dº país:" %(x+1)))
    totMedalhas = qtdOuro*3+qtdPrata*2+qtdBronze*1
    tmp.append(totMedalhas)
    paises.append(tmp)
    x+=1

pais1,pais2,pais3,medal1,medal2,medal3 = paises[0][0],paises[1][0],paises[2][0],paises[0][1],paises[1][1],paises[2][1]

if paises[0][1]>paises[1][1]:
    if paises[0][1]>paises[2][1]:
        if paises[1][1]>paises[2][1]:
            print("O primeiro colocado foi o %s com %d medalhas."%(pais1,medal1))
            print("O segundo colocado foi o %s com %d medalhas." % (pais2,medal2))
            print("O terceiro colocado foi o %s com %d medalhas." % (pais3,medal3))
        else:
            print("O primeiro colocado foi o %s com %d medalhas." %(pais1,medal1))
            print("O segundo colocado foi o %s com %d medalhas." % (pais3,medal3))
            print("O terceiro colocado foi o %s com %d medalhas." % (pais2,medal2))
if paises[1][1]>paises[0][1]:
    if paises[1][1] > paises[2][1]:
        if paises[0][1] > paises[2][1]:
            print("O primeiro colocado foi o %s com %d medalhas." % (pais2,medal2))
            print("O segundo colocado foi o %s com %d medalhas." % (pais1,medal1))
            print("O terceiro colocado foi o %s com %d medalhas." % (pais3,medal3))
        else:
            print("O primeiro colocado foi o %s com %d medalhas." % (pais2,medal2))
            print("O segundo colocado foi o %s com %d medalhas." % (pais3,medal3))
            print("O terceiro colocado foi o %s com %d medalhas." % (pais1,medal1))
if paises[2][1]>paises[0][1]:
    if paises[2][1] > paises[1][1]:
        if paises[0][1] > paises[1][1]:
            print("O primeiro colocado foi o %s com %d medalhas." % (pais3,medal3))
            print("O segundo colocado foi o %s com %d medalhas." % (pais1,medal1))
            print("O terceiro colocado foi o %s com %d medalhas." % (pais2,medal2))
        else:
            print("O primeiro colocado foi o %s com %d medalhas." % (pais3,medal3))
            print("O segundo colocado foi o %s com %d medalhas." % (pais2,medal2))
            print("O terceiro colocado foi o %s com %d medalhas." % (pais1,medal1))