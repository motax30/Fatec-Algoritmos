x=1
H=0
l=[]
acm = 1
print("Algoritmo de Soma dos primeiros termos da série H.")
while x<=8:
    y=acm
    while y<=acm+2:
        if y<acm+2:
            H+=1/(y**3)
            l.append(H)
        elif y<10:
            H-=1/(y**3)
            l.append(H)
        y+=2
    acm+=4
    x+=1
print("O valor do %d primeiros termo da série H = %f"%(len(l),H))
