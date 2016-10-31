print("Algoritmo inversão de um número de 3 dígitos fornecido pelo usuário!")
n1 = int(input("Informe um número de 3 dígitos"))
if n1>100:
    if n1<=999:
        v= str(n1)
        u = v[2:]
        d = v[1:-1]
        c = v[:-2]
        invert = u + d + c
        print("O número %d em sua forma invertida é: %s" % (n1, invert))
    else:
        print("Inválido, você deve informar um número com 3 dígitos.")
else:
    print("Inválido, você deve informar um número com 3 dígitos.")