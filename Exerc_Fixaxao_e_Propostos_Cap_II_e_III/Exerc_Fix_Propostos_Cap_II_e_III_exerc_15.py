n1,n2 = int(input("Insira o primeiro número:")),int(input("Insira o segundo número:"))
x=0
while n1>=n2:
    n1=n1-n2
    x+=1
print("O quociente da divisão de n1 por n2 é:%d"%x)