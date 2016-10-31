print("Algoritmo informando o nome do mês")
mes = int(input("Informe um número de 1 à 12 para saber o mês"))
x=1
meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
while x<=12:
    if mes==x:
        print("O mês escolhido foi %s"%meses[x-1])
    x+=1
