print("Algoritmo Cálculo do consumo de um veículo!")
kmInicial = 0
cap = int(input("Informe a capacidade do tanque do veículo:"))
tanqueCheio = cap
qtdLitros = int(input("Informe a quantidade de litros a ser abastecido:"))
kmPerc =  int(input("Informe a kilometragem percorrida desde o último abastecimento"))
consumo = kmPerc/qtdLitros
cap = cap-consumo
autonomia = cap

