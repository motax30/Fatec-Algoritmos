print("Algoritmo Prestação em atraso")
preAtraso = float(input("Informe o valor da prestação em atraso:"))
acres = preAtraso*0.1
desc = acres*0.1
vfinal = preAtraso+acres+desc
prejuizo = vfinal-preAtraso
print("Para a prestação %.2f o valor final foi de R$ %.2f, o comerciante maluco teve um prejuizo de: R$ %.2f"%(preAtraso,vfinal,prejuizo))