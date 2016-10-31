print("Algoritmo Mínimo multiplo comum entre dois números!")
n1,n2 = int(input("Informe o primeiro número")),int(input("Informe o segundo número"))
tmpn1 = []
tmpn2 = []
fatoriais = []
for i in range(2,n1,1):
    r = n1%i
    z=n1/i
    if r==0:
        tmpn1.append(i)
for i in range(2,n2,1):
    r2 = n2%i
    z = n2/1
    if r2==0:
        tmpn2.append(i)
if len(tmpn1)>len(tmpn2):
    for i in range(0,len(tmpn1)):
        if fatoriais[i]!=tmpn1[i]:
            fatoriais.append(tmpn1[i])
        if fatoriais[i]!=tmpn1[i]:
            fatoriais.append(tmpn2[i])
mmc = 1
for i in range(1,len(fatoriais)):
    mmc*=fatoriais[i]
print("O mmc dos números fornecidos é: %d"%mmc)

mmc = tmpn1*tmpn2
print("O mmc entre os dois números fornecidos é: %.2f"%mmc)