numTotalCriancas = 0
totPrematuro = 0
totPrematMasc = 0
totPrematFem = 0
totDiasIncub = 0
diasIncub = []
sexoPremat = []
cont = 1
while cont>0:
    print("Para encerrar a execução do programa digite 'x' quando solicitado o sexo")
    sexo = input("Informe o sexo da %dº criança, (M)Masculino ou (F)Feminino:"%cont)
    if sexo == "X" or sexo=="x":
        break
    elif sexo == "M" or sexo == "m" or sexo == "Masculino" or sexo == "masculino" or sexo == "f"or sexo == "F"or sexo == "Feminino" or sexo == "feminino":
        prematuro = input("Informe se a %dº criança é prematura, (S)Sim ou (N)Não: "%cont)
        if prematuro =="s" or prematuro =="sim" or prematuro =="Sim":
            totPrematuro += 1
            if sexo=="m" or sexo=="M":
                totPrematMasc+=1
                diasIncubadora = int(input("Informe quantos dias o %dº recém-nascido permaneceu na incubadora:"%cont))
                totDiasIncub += diasIncubadora
                diasIncub.append(diasIncubadora)
                sexoPremat.append("Masculino")
                numTotalCriancas = numTotalCriancas + 1
                cont += 1
            elif sexo=="f" or sexo=="F":
                totPrematFem += 1
                diasIncubadora = int(input("Informe quantos dias a %dº recém-nascida permaneceu na incubadora:"%cont))
                totDiasIncub += diasIncubadora
                diasIncub.append(diasIncubadora)
                sexoPremat.append("Feminino")
                numTotalCriancas = numTotalCriancas + 1
                cont += 1
            else:
                print("Caracter informado inválido.")
        elif prematuro =="n" or prematuro =="não" or prematuro =="Não":
            numTotalCriancas=numTotalCriancas+1
            cont+=1
        else:
            print("Caracter informado inválido.")
    else:
        print("Caracter informado inválido.")
if numTotalCriancas==0:
    print("Você não informou nenhum dado de recém nascido!\n Fim do Programa!")
else:
    qtdRecemNascPremat = len(diasIncub)
    percPrematuro = (totPrematuro*100)/numTotalCriancas
    percRecNascMasc = (totPrematMasc*100)/qtdRecemNascPremat
    percRecNascFem = (totPrematFem*100)/qtdRecemNascPremat
    mediaIncubadora = totPrematuro/qtdRecemNascPremat
    maiorNumDias = max(diasIncub)
    print("Quadro demonstrativo:\n")
    print("A quantidade total de crianças nascidas no período foi de: %d crianças. "%numTotalCriancas)
    i=0
    while i < len(sexoPremat):
        print("O sexo do %dº prematuro é %s e permaneceu %d dias na incubadora."%(i+1,sexoPremat[i],diasIncub[i]))
        i+=1
    print("A porcentagem de recém nascidos prematuros é de %.2f%%"%percPrematuro)
    print("A porcentagem de recém-nascidos meninos do total de prematuros é de: %.2f%%"%percRecNascMasc)
    print("A porcentagem de recém-nascidos meninas do total de prematuros é de: %.2f%%"%percRecNascFem)
    print("A média de dias de permanência dos recém nascidos prematuros na incubadora é de: %.2f"%mediaIncubadora)
    print("O maior número de dias que um recém-nascido prematuro permaneceu na incubadora foi de: %.2f dias"%maiorNumDias)
    print("Fim do Programa.")