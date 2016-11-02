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
for i in range(0,len(palavra)):
    n = random.randrange(0,len(palavra))
    embaralhada +=palavra[n]
print("%s"%embaralhada)
x=0
while x<6:
    tentativa = input("%dº tentativa, digite uma palavra para adivinhar a palavra embaralhada:"%(x+1))
    if tentativa == palavra:
        print("Parabéns, você acertou a palavra que é:%s."%palavra)
        break
    else:
        print("%s" % embaralhada)
        print("Você ainda tem %d tentativa(s)."%(x+2))
    x+=1
if x==6:
    print("Você excedeu o número de tentativas, a palavra a ser adivinhada é: %s"%palavra)