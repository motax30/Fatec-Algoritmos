import random
"""Jogo da palavra embaralhada. Desenvolva um jogo
em que o usuário tenha que adivinhar uma palavra
que será mostrada com as letras embaralhadas. O
programa terá uma lista de palavras lidas de uma
lista (previamente definhada com 10 palavras) e
escolherá uma aleatoriamente. O jogador terá seis
tentativas para adivinhar a palavra.
Ao final a palavra deve ser mostrada na tela,
informando se o usuário ganhou ou perdeu o jogo"""
embaralhada = ""
palavras = ["amendoas","gabriela","Alfredo","Alemanha","Uruguai","venezuela","algoritmo","João", "paralelepípedo", "parlamentar"]
print("Tente adivinhar a palavra embaralhada abaixo:")
palavra = random.choice(palavras)
aux = palavra
while True:
    tam_embaralhada = len(embaralhada)
    tam_palavra = len(palavra)
    if tam_embaralhada<tam_palavra:
        i = random.randint(0,(len(aux)-1))
        letra = aux[i]
        embaralhada +=letra
        a,b = "",""
        for j in range(0,len(aux)):
            if j!=i:
                a+=aux[j]
            else:
                b+=aux[j]
        if len(a)>=len(b):
            aux = a
        else:
            aux = b
            break
print("%s"%embaralhada)
x=1
while x<=6:
    tentativa = input("%dº tentativa, digite uma palavra para adivinhar a palavra embaralhada:"%(x))
    if tentativa == palavra:
        print("Parabéns, você acertou, a palavra é:%s."%palavra)
        break
    else:
        print("%s" % embaralhada)
        print("Você ainda tem %d tentativa(s)."%(6-x))
    x+=1
if x==0:
    print("Você excedeu o número de tentativas, a palavra a ser adivinhada é: %s"%palavra)