from datetime import date
dia = int(input("Informe o dia do seu aniversário com dois digitos:"))
mes = int(input("Informe o mês do seu aniversário com dois dígitos:"))
ano = int(input("Informe o do seu aniversário com quatro dígitos:"))
diaAtual = date.today().day
mesAtual = date.today().month
anoAtual = date.today().year
print("---------------------------------------Algoritmo cálculo da idade---------------------------------------\n")

anos = anoAtual-ano
meses = mesAtual - mes
dias = mesAtual-mes
idade = ""
if(anos>1):
    idade+= "Você tem %d anos, " % anos
else:
    idade+= "Você tem %d ano, " % anos
if(meses>1):
    idade+= "%d meses e " % meses
else:
    idade+= "%d mês e " % meses
if(dias>1):
    idade+= "%d dias e " % dias
else:
    idade+= "%d dia." % dias
print(idade)

