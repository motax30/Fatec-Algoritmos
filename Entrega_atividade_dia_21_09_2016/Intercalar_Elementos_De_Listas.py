from _sitebuiltins import _Printer

print("Programa para intercalar listas")
l1=[]
l2=["a","b","c","d","e","f","g","h","i"]
l3=[]
i=1
while i<=25:
    l1.append(i)
    i+=1
for w in range(0,len(l1)):
    l3.append(l1[w])
    if(w<len(l2)):
        l3.append(l2[w])
print("Lista 1:"+str(l1))
print("Lista 2:"+str(l2))
print("Lista 3:"+str(l3))

