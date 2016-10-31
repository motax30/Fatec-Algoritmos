print("Algoritmo para verificar se um número é primo ou não!")
n1 = int(input("Informe um número para saber se é primo"))
divisores = []
i=0
acmDiv = ""
while i<=n1:
    if n1%(i+1)==0:
       divisores.append(i+1)
    i+=1
if divisores[0]==1 and divisores[1]==n1:
    print("O númenro %d é primo"%n1)
else:
    z = 1
    acmDiv=str(divisores[0])
    while z<len(divisores)-1:
        acmDiv=acmDiv+","+str(divisores[z])
        z+=1
    print("O número %d não é primo pois ele é divisível por %s"%(n1,acmDiv))