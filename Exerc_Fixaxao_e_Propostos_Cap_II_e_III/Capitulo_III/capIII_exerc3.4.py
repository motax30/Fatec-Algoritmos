print("Algoritmo Geração do número H")
n = int(input("Informe um número:"))
H = 1
for i in range(1,n):
    H=H+(1/i)
print("O número H é igual a: %.2f"%H)