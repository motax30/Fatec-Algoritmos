print("Algoritmo Fatorial do número 'n'")
n = int(input("Informe um número:"))
x=1
acm = 1
fat = "1"
while x<=n:
    acm*=x+1
    fat+="x"+str(acm)
    x+=1
print("O fatorial de %d é igual a: %s = %d"%(n,fat,acm))