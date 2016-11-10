print("Jogo Batalha Naval")
arq1 = open('jogador1.txt','r').readlines()
arq2 = open('jogador2.txt','r').readlines()
j1 = []
j2 = []

pecasPosicionadas_j1 = ''
pecasPosicionadas_j2 = ''
col = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]

def preencherTabuleiroVazio(posicoes):
    for l in range(0,len(col)):
        for j in range(1, 16):
            posicoes+= col[l] + str(j) + ",0|"
    return posicoes

tabul_j1 = preencherTabuleiroVazio(pecasPosicionadas_j1)
tabul_j2 = preencherTabuleiroVazio(pecasPosicionadas_j2)

def extrairPecasDosArquivos():
    i = 0
    while i<=3:
        cod_j1 = (arq1[i].split("; "))[0].split(";")[0]
        posicao_direcao_j1 = (arq1[i].split("; "))[0].split(";")[1].replace("\n","").split("|")
        j = [cod_j1]
        for p in range(len(posicao_direcao_j1)):
            j.append(posicao_direcao_j1[p])
        j1.append(j)
        cod_j2 = (arq2[i].split("; "))[0].split(";")[0]
        posicao_direcao_j2 = (arq2[i].split("; "))[0].split(";")[1].replace("\n", "").split("|")
        k = [cod_j2]
        for p in range(len(posicao_direcao_j2)):
            k.append(posicao_direcao_j2[p])
        j2.append(k)
        i+=1

def getIndicePecaJogador(jogador,termoPesquisado):
    for j in range(len(jogador)):
            for i in range(len(jogador[j])):
                if termoPesquisado == jogador[j][i]:
                    return j,i

def getElementosDaPeca(codPeca, posPeca, horientacao):
    qtd_Encouracados,qtd_portaAvioes,qtd_Submarinos,qtd_Cruzadores = 2,2,5,4
    elem = ""
    elementos = ""
    i = 0
    linhaPeca = str
    colPeca = int
    if len(posPeca)<4:
        linhaPeca = posPeca[0]
        colPeca = int(posPeca[1])
    else:
        linhaPeca = posPeca[0]
        colPeca = int(posPeca[1]+posPeca[2])
    if horientacao=="H":
        if codPeca == 1:
            while i<qtd_Encouracados:
                elem+=(linhaPeca+str(colPeca)+",1|")
                i+=1
                colPeca+=1
            elementos = elem
        elif codPeca == 2:
            while i<qtd_portaAvioes:
                elem+=(linhaPeca+str(colPeca)+",1|")
                i+=1
                colPeca+=1
            elementos = elem
        elif codPeca == 3:
            linhaPeca = posPeca[0]
            colPeca= int(posPeca[1])
            elementos = (linhaPeca+str(colPeca)+",1|")
        elif codPeca == 4:
            while i<qtd_Cruzadores:
                elem+=(linhaPeca+str(colPeca)+",1|")
                i+=1
                colPeca+=1
            elementos = elem
    elif horientacao=="V":
        colLetra=col.index(linhaPeca)
        if codPeca == 1:
            while i<qtd_Encouracados:
                elem+=(col[colLetra]+str(colPeca)+",1|")
                i+=1
                colLetra+=1
            elementos = elem
        elif codPeca == 2:
            while i< qtd_portaAvioes:
                elem += (col[colLetra] + str(colPeca) + ",1|")
                i += 1
                colLetra += 1
            elementos = elem
        elif codPeca == 3:
            elementos = (col[colLetra] + str(colPeca) + ",1|")
        elif codPeca == qtd_Cruzadores:
            while i<4:
                elem += (col[colLetra] + str(colPeca) + ",1|")
                i += 1
                colLetra += 1
            elementos = elem
    elif horientacao=="N/A":
        colLetra = col.index(linhaPeca)
        elementos = (col[colLetra] + str(colPeca) + ",1|")
    return elementos

def posicionarPecasJogador(jogador,tabuleiroVazio):      #Passar como parâmetro a lista das posições do Jogador: J1 ou J2
    for c in range(0,len(jogador)):
        cod = getIndicePecaJogador(jogador, jogador[c][0])
        for d in range(0,len(jogador[c])-1):
            peca = getIndicePecaJogador(jogador,jogador[c][d+1])
            pos = jogador[peca[0]][peca[1]]
            if len(pos)>=3:
                pos = pos[len(pos)-1:]
            else:
                pos = 'N/A'
            peca= getElementosDaPeca(int(jogador[cod[0]][cod[1]]), jogador[peca[0]][peca[1]], pos).split('|')
            adicionarElementosPecaNoTabuleiro(peca,tabuleiroVazio,pos)

def adicionarElementosPecaNoTabuleiro(peca,tabuleiroVazio,posicao):
    f = 0
    while f < len(peca) - 1:
        global temp
        if len(peca[f]) < 5:
            velho = peca[f][:len(peca[f]) - 2] + ",0"
            novo = peca[f]
        else:
            velho = peca[f][:len(peca[f]) - 2] + ",0"
            novo = peca[f]
        if tabuleiroVazio == tabul_j1:
            if velho in tabul_j1:
                k = temp.replace(velho, novo)
                temp = k
        elif tabuleiroVazio == tabul_j2:
            if velho in tabul_j2:
                k = temp.replace(velho, novo)
                temp = k
        else:
            print("Posição %s está fora dos limites do tabuleiro.Esta posição pertence à peça %s"
                  "" % (velho[:-2], peca[0][:-2] + posicao))
            return False
            break
        f+=1

temp = tabul_j1
extrairPecasDosArquivos()
posicionarPecasJogador(j1,tabul_j1)
pecasPosicionadas_j1= temp
temp = tabul_j1
posicionarPecasJogador(j2,tabul_j2)
pecasPosicionadas_j2= temp
print(pecasPosicionadas_j1)
print(pecasPosicionadas_j2)