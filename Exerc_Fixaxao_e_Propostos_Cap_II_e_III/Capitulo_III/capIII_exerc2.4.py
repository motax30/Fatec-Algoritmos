print("Algoritmo Cálculo do Peso Total")
print("--------------------------------------------------------------------------------------------")
alt = float(input("Insira sua altura: "))
sexo = input("Insira seu sexo, (M)Masculino ou (F)Feminino:")
if((sexo=="M") or (sexo=="m")):
    peso = (72.7*alt)-58
    print("Você é do sexo masculino e seu peso ideal é de: %f" %peso)
elif((sexo=="F") or (sexo=="f")):
    peso = (62.1*alt)-44.7
    print("Você é do sexo feminino e seu peso ideal é de: %f" % peso)
