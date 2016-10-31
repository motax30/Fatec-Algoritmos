print("Algoritmo para cálculo do IMC de uma pessoa\n"
      "Tabela demonstrativa do IMC\n"
      "")
p,a, = int(input("Informe seu peso:")),float(input("Informe sua altura:"))
imc = p/a**2
if imc<18.5:
    print("Seu IMC é: %d e você está abaixo do peso!"%imc)
elif imc<25:
    print("Seu IMC é: %d e você está com o peso normal!" % imc)
elif imc<30:
    print("Seu IMC é: %d e você está acima do peso!" % imc)
elif imc>=30:
    print("Seu IMC é: %d e você está obeso!" % imc)
print("Fim do Programa")