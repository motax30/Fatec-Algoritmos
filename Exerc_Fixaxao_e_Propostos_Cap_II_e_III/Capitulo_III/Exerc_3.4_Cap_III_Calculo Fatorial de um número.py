print("Algoritmo Cálculo Fatorial de um número!")
n1 = int(input("Informe um número:"))
x=2
fat = 1
result = 1
if n1==1 or n1==0:
    print("O fatorial de %d é = 1"%n1)
else:
    while x<=n1:
        fat = str(fat)+"x"+str(x)
        result*=x
        x+=1
    print("O fatorial do número %d = %s = %.2f"%(n1,fat,result))