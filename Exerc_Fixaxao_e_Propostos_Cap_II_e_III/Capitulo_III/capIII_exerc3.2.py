print("Algoritmo Impressão numero que mais se aproxima da raiz quadrada de um número fornecido pelo usuário")
a = int(input("Informe um número:"))
quadrado = a**(1/2)
menor = quadrado-1
print("O número que mais se aproxima da raiz quadrada de %d é: %d"%(a,menor))

