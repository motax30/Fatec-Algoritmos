x=1
l = []
print("Algoritmo Maior e menor valor informado pelo usuário!")
while x<=20:
    v= int(input("Informe o %dº número:"%x))
    print("Caracter(es) informado(s) inválido(s)")
    l.append(v)
    x+=1
maior = max(l)
menor = min(l)
print("O maior número fornecido foi: %d e o menor foi: %d"% (maior,menor))
