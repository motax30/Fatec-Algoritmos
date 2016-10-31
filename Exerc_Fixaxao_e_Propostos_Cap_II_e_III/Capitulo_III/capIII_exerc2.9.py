print("Algoritmo Cálculo operação aritmética fornencendo-se a operação desejada\n"
      "-------------------------------------------------------------------------")
oper,r,n1,n2,op ="", 0,int(input("Informe o primeiro número:")),int(input("Informe o segundo número:")),input("Informe a operação aritmética desejada\n(+)Adição;\n(-)Subtração\n(*)Multiplicação\n(/)Divisão:")
while True:
    if op=="+":
        oper="Adição"
        r=n1+n2
        break
    elif op=="-":
        if n1>n2:
            oper="Subtração"
            r=n1-n2
            break
        else:
            oper="Subtração"
            r=n2-n1
            break
    elif op=="*":
        oper = "Multiplicação"
        r = n1 * n2
        break
    elif op=="/":
        if n1>n2:
            oper = "Divisão"
            r=n1/n2
            break
        else:
            oper = "Divisão"
            r=n2/n1
            break
    else:
        print("Caracter inválido")
if n1>n2:
    print("O resultado da operação de %s de %d por %d = %d "%(oper,n1,n2,r))
else:
    print("O resultado da operação de %s de %d por %d = %d " %(oper, n2, n1, r))