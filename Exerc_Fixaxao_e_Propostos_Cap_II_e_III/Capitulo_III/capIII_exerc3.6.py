a,b=0,1
x=0
fib=['1']
print("Algoritmo Fibonacci")
while x<10:
    a+=b
    b+=a
    fib.append(str(a))
    fib.append(str(b))
    x+=1
elementos = ""
for i in range(0,len(fib)-1):
    elementos+=fib[i]+","
print("Fibonacci dos %d primeiros termos é: %s"%(len(fib)-1,elementos[:-1]))