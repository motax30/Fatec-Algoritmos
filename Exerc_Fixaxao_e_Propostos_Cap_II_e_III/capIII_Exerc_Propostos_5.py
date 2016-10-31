print("Algoritmo Cálculo idade com uma data de aniversário fornecida!")
idade = []
anoNiver = 1985
mesNiver = 9
diaNiver = 12
ano = int(input("Informe o ano atual"))
mes = int(input("Informe o mÊs atual"))
dia = int(input("Informe o dia atual"))
dt1 = anoNiver*365+mesNiver*30+diaNiver
dt2 = ano*365+mes*30+dia
x = dt2-dt1
z = x%365
a,m,d = int(x/365),int((x%365)/30),int((x%365)%30)
idade.append(a)
idade.append(m)
idade.append(d)
print("A idade calculada é: %d anos, %d meses e %d dias"%(idade[0],idade[1],idade[2]))