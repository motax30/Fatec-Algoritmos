print("Algoritmo Categoria de um nadador")
print("--------------------------------------------------------------------------------------------")
idade = int(input("Digite um código para ver sua classificação, conforme mostrado acima: "))
if(idade<=4):
    print("Você ainda não pode nadar")
elif(idade<=7):
    print("Sua categoria é Infantil A")
elif(idade<=10):
    print("Sua categoria é Infantil B")
elif(idade<=13):
    print("Sua categoria é Juvenil A")
elif(idade<=17):
    print("Sua categoria é Juvenil B")
else:
    print("Sua categoria é Adulto")

