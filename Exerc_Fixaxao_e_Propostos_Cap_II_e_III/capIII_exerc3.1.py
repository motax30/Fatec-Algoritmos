a = int
b=int
i=int
j=int
a = int(input("Informe o valor de a:"))
for i in range(1,a):
    j=i
    while j<=a:
        print(j)
        j=j+1
    b=a
while ((a-b) or (a<=0)):
    for i in range(1,a):
        j=i
        while j<=a:
            print(j)
            j=j+1
    b = a
    a = int(input("Informe o valor de a:"))