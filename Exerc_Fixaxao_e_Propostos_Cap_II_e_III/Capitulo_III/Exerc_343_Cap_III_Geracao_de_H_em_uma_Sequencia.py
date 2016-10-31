print("Algoritmo para geração da variável H de uma sequência!")
n1 = int(input("Informe um número:"))
x=2
H = 1
l = "1"
for i in range(2,n1+1):
    H += (1 / i)
    item = "1/%d"%i
    if i<=n1:
        l=l+"+"+item
print("O valor de H = %s = %.2f"%(l,H))
