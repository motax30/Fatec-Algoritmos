a=[1,2,3,4,5,6,7,8,9,10]
c=[]
col1=[]
col2=[]
col3=[]
for i in range(0,len(a)):
    w=a[i]
    w+=5
    col1.append(w)
for i in range(0,len(a)-1):
    fat=1
    for j in range(0,a[i+1]):
        fat*=j+1
    col2.append(fat)
for i in range(0, len(a)):
    z = a[i]
    z = z ** 2
    col3.append(z)
for i in range(0, len(a) - 1):
    tmp = []
    tmp.append(col1[i])
    tmp.append(col2[i])
    tmp.append(col3[i])
    c.append(tmp)
    print(c[i])