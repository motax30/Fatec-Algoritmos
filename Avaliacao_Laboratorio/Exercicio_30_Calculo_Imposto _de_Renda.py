print("Algoritomo Cálculo de Imposto de Renda de 10 Contribuintes\n"
      "----------------------------------------------------------")
contribuinte = 1
salMin = 880
imp = []
isent = []
numCPF = []
while contribuinte<=10:
    cpf = int(input("Informe o número do CPF do %dº contribuinte:"%contribuinte))
    numDep = int(input("Informe o número de dependentes do %dº contribuinte:"%contribuinte))
    renda = float(input("Informe a renda do %dº contribuinte:"%contribuinte))
    descDependente = (salMin * 0.05)*numDep
    if renda<=2*salMin:
        imp.append("isento")
        numCPF.append(cpf)
    elif renda<=3*salMin:
        imposto =(renda*0.05)+descDependente
        imp.append(imposto)
        numCPF.append(cpf)
    elif renda<=5*salMin:
        imposto = (renda*0.1) + descDependente
        imp.append(imposto)
        numCPF.append(cpf)
    elif renda<=7*salMin:
        imposto = (renda*0.15) + descDependente
        imp.append(imposto)
        numCPF.append(cpf)
    elif renda>=7*salMin:
        imposto = (renda*0.2) + descDependente
        imp.append(imposto)
        numCPF.append(cpf)
    contribuinte+=1
i=0
while i <len(imp):
    ncpf = numCPF[i]
    impDev = imp[i]
    if impDev=="isento":
        print("O %d º contribuinte é isento"%i+1)
    else:
        print("O imposto devido pelo %d º contribuinte é de CPF nº %d é de R$ %.2f."%(i+1,ncpf,impDev))
    i+=1