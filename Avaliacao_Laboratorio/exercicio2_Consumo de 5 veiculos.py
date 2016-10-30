l1 = []
l2 = []
c=1
while c<=5:
    l1.append(input("Informe o %dº veículo:"%c))
    l2.append(int(input("Informe o consumo do %dº veículo:"%c)))
    c+=1
qtdLitros = []
custoCarro = []
a=0
maisEconomico = min(l2)
indMaisEcononomico = l2.index(min(l2))

w=0
while w < len(l1):
    qtdLitros.append(1000/l2[w])
    custoCarro.append(qtdLitros[w]*2.25)
    print("Veículo %i\n Nome: %s\n Km por litro: %.2f"%(w+1,l1[w],l2[w]))
    w+=1

print("\n")
print("Relatório Final\n")
j=0
while j < len(l1):
    print("%d  -  %s   %.2f km/Litro   - %d litros      - R$ %.2f."%(j+1,l1[j],l2[j],qtdLitros[j],custoCarro[j]))
    j+=1
print("O menor consumo é do %s "%l1[indMaisEcononomico])