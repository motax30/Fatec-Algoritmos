print("Algoritmo Fibonacci até o 20º termo!")
a,b= 0,1
seq = 0
fib=1
l = []
while seq<20:
    l.append(a)
    l.append(b)
    a=a+b
    b=b+a
    seq+=1

print(fib)