print("Algoritmo Numero mais se aproxima da Raiz quadrada do número fornecido pelo usuário")
n1 = int(input("Informe um número:"))
raiz = n1**(1/2)
antes=raiz-1
depois = raiz+1
print("O números que mais se aproximam da raiz quadrada do número informado são:%d e %d"%(antes,depois))