from random import randint
lista = ["leão","tigre","elefante","puma","foca"]
dica = "Dica: A palavra a ser adivinhada é um animal!!!"
tamanhoLista = len(lista)
rand = randint(0,tamanhoLista-1)
palavra = lista[rand]
tamanhoPalavra = len(palavra)
print("---------------------------------Jogo da Adivinhação---------------------------------\n"
      "Regras:\n"
      "1 - O jogador terá 5 (cinco) tentativas para adivinhar a palavra + a tentativa final que comparará a palavra toda;\n"
      "2 - Caso você digite mais de uma letra em alguma de suas tentativas o jogo comparará a palavra digitada com a palavra sorteada\n"
      "e verificará se foi informada a palavra correta. Em caso positivo, apresentará a mnesagem: Parabéns, você acertou a palavra!”\n"
      "Em caso negativo, apresentará: 'Tente novamente.', mostrará a palavra a ser adivinhada e encerrará o programa!")
resp = []
i=0
while i<tamanhoPalavra:
    resp.append(" _ ")
    i+=1

qtdTentativas = 5
tentativaAtual = ""
print("_ "*len(palavra)+"(%d Letras)"%tamanhoPalavra)

while qtdTentativas>=0:
    if qtdTentativas>=1:
        if qtdTentativas>1:
            print("%s.\nVocê tem %d tentativas." % (dica,qtdTentativas))
        else:
            print("%s.\nVocê tem %d tentativa." % (dica, qtdTentativas))
        LetraOuPalavraInformada = input("Digite uma letra ou a palavra a adivinhar:").lower()
        print("")
        if len(LetraOuPalavraInformada)==1:
            w=0
            while w<tamanhoPalavra:
                espaco = palavra[w].lower()
                if(espaco==LetraOuPalavraInformada):
                    resp[w]=LetraOuPalavraInformada
                else:
                    resp[w]=resp[w]
                w+=1
            temp = ""
            tentativaAtual = ""
            j=0
            while j<len(resp):
                tentativaAtual += resp[j]
                j+=1
            print("%s(%d Letras)" % (tentativaAtual, tamanhoPalavra))
            qtdTentativas-=1
        elif LetraOuPalavraInformada==palavra:
            print("Parabéns, você acertou a palavra!.")
            break
        else:
            print("Tente novamente. A palavra correta é: %s "%palavra)
            break
    else:
        palavraCompleta = input("Esta é sua tentativa final, você deve digitar toda a palavra para tentar acertar:").lower()
        if palavraCompleta == palavra:
            print("Parabéns, você acertou a palavra!.")
            break
        else:
            print("Você excedeu o número de (5) tentativas simples e a tentativa final, a palavra correta é:%s "%palavra)
            break