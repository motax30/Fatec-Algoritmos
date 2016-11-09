print("Jogo Batalha Naval")
arq1 = open('jogador1.txt','r').readlines()
arq2 = open('jogador2.txt','r').readlines()
j1 = []
j2 = []
i=0
tabuleiro_vazio = ""
col = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]

for l in range(0,len(col)):
    for j in range(1, 16):
        tabuleiro_vazio+= col[l]+str(j)+",0|"

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
    for j in range(len(j1)):
            for i in range(len(j1[j])):
                if termoPesquisado == jogador[j][i]:
                    return j,i

def montarPecas(codPeca, posPeca, horientacao):
    elem = ""
    i = 0
    linhaPeca = posPeca[0]
    colPeca = int(posPeca[1])
    if horientacao=="H":
        if codPeca == 1:
            while i<4:
                elem+=(linhaPeca+str(colPeca)+",1|")
                i+=1
                colPeca+=1
            elementos = elem
        elif codPeca == 2:
            while i<5:
                elem+=(linhaPeca+str(colPeca)+",1|")
                i+=1
                colPeca+=1
            elementos = elem
        elif codPeca == 3:
            linhaPeca = posPeca[0]
            colPeca= int(posPeca[1])
            elementos = (linhaPeca+str(colPeca)+",1|")
        elif codPeca == 4:
            while i<2:
                elem+=(linhaPeca+str(colPeca)+",1|")
                i+=1
                colPeca+=1
            elementos = elem
    elif horientacao=="V":
        colLetra=col.index(linhaPeca)
        if codPeca == 1:
            while i<4:
                elem+=(col[colLetra]+str(colPeca)+",1|")
                i+=1
                colLetra+=1
            elementos = elem
        elif codPeca == 2:
            while i<5:
                elem += (col[colLetra] + str(colPeca) + ",1|")
                i += 1
                colLetra += 1
            elementos = elem
        elif codPeca == 3:
            elementos = (col[colLetra] + str(colPeca) + ",1|")
        elif codPeca == 4:
            while i<2:
                elem += (col[colLetra] + str(colPeca) + ",1|")
                i += 1
                colLetra += 1
            elementos = elem
    elif horientacao=="N/A":
        colLetra = col.index(linhaPeca)
        elementos = (col[colLetra] + str(colPeca) + ",1|")
    return elementos
def posicionarPecasJogador(jogador):      #Passar como parâmetro a lista das posições do Jogador: J1 ou J2
    global tabuleiro
    for c in range(len(jogador)):
        cod = getIndicePecaJogador(jogador, jogador[c][0])
        for d in range(0,len(jogador[c])-1):
            peca = getIndicePecaJogador(jogador,jogador[c][d+1])
            pos = jogador[peca[0]][peca[1]]
            if len(pos)>=3:
                pos = pos[len(pos)-1:]
            else:
                pos = 'N/A'
            peca= montarPecas(int(jogador[cod[0]][cod[1]]), jogador[peca[0]][peca[1]], pos).split('|')
            f=0
            while f<len(peca)-1:
               # ind = tabuleiro.find(peca[0][:2])
                velho  = peca[f][:len(peca[f])-1]+"0"
                novo = peca[f]
                tabuleiro = tabuleiro.replace(velho,novo)
                ct = tabuleiro.count(',1')
                f+=1
    return tabuleiro
tabuleiro_j1 = posicionarPecasJogador(j1)
tabuleiro_j2 = posicionarPecasJogador(j2)
