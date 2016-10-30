import math
print("Programa para calcular e Demonstrar as Médias de Idade dos alunos de uma sala!!!!")
print("------------------------------------------------------------------------------------------------------------------")
totIdade=0
qtdAlunos = 0
somaHarmonica = 0
produtorioIdades = 1
idade=int
while True:
    idade = int(input("Informe as idades dos alunos da turma e para imprimir os resultados, digite (0): "))
    if(idade>0): 
        totIdade = totIdade+idade
        produtorioIdades = produtorioIdades*idade
        somaHarmonica = somaHarmonica+(1/produtorioIdades)
        qtdAlunos+=1
    if(idade==0):
        break
 
ma = totIdade/qtdAlunos
mg = math.pow(produtorioIdades,(1/qtdAlunos))
mharm=qtdAlunos/somaHarmonica
desvPop = math.sqrt(((((qtdAlunos*(totIdade))**2)-(totIdade**2))/qtdAlunos**2))
desvAmost= math.sqrt((((qtdAlunos*(totIdade)**2)-(totIdade**2))/(qtdAlunos*(qtdAlunos-1))))
print("A média Aritmédica dos alunos é de: %f"%ma)
print("A média Geométrica dos alunos é de: %f"%mg)
print("A média Harmônica dos alunos é de: %f"%mharm)
print("O desvio populacional dos alunos é de: %f"%desvPop)
print("O Desvio amostra dos alunos é de: %f"%desvAmost)
print("-----------------------------------------------------------------------------------------------------------------")
