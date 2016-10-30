print("Algoritmo Operações Matematicas")
print("----------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------")
n1=int(input("Insira o primeiro número"))
n2=int(input("Insira o segundo número"))
op=input("Qual operação você deseja efetuar?\n(1) Adição, (2)Subtração, (3)Multiplicação, (4)Divisão, (5)Exponenciação")
if(op=="1"):
    result=n1+n2
    tipoOp = "Adição"
    print("Operação de %s: %d + %d = %d."%(tipoOp,n1,n2,result))
elif(op=="2"):
    result=n1-n2
    tipoOp = "Subtração"
    print("Operação de %s: %d - %d = %d."%(tipoOp,n1,n2,result))
elif(op=="3"):
    result=n1*n2
    tipoOp = "Multiplicação"
    print("Operação de %s: %d * %d = %d."%(tipoOp,n1,n2,result))
elif(op=="4"):
    result=n1/n2
    tipoOp = "Divisão"
    print("Operação de %s: %d / %d = %d."%(tipoOp,n1,n2,result))
elif(op=="5"):
    result=n1**n2
    tipoOp = "Potencição"
    print("Operação de %s: %d ** %d = %d."%(tipoOp,n1,n2,result))
print("----------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------")
print("------------------------------------------Fim do Programa-------------------------------------------------------")