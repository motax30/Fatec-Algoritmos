print("Algoritmo média ponderada")
l = []
medias=[]
somatorio = 0
x=1
while x<=5:
    n1 = int(input("Informe o %dº número:"%x))
    l.append(n1)
    x+=1
for i in range(0,len(l)):
    elem = l[i]*(i+1)
    medias.append(elem)
    somatorio+=elem
mp = somatorio/5
print("A média ponderada dos números fornecidos é:%.2f"%mp)