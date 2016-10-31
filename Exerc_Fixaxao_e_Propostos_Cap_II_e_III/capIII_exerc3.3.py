print("Algoritmo Número é primo ou não")
a = int(input("Informe um número:"))
acm = 0
l = ""
for i in range(1,a+1):
    if a%i==0:
        acm+=1
        l+=","+str(i)
if acm<=2:
    print("O número %d é primo, pois ele é divisível por %s ."%(a,l[1:]))
else:
    print("O número %d não é primo." %(a))


