print("Jogo Batalha Naval")
arq1 = open('jogador1.txt','r').readlines()
arq2 = open('jogador2.txt','r').readlines()
j1 = []
j2 = []
i=0
tabuleiro_vazio = ""
tabuleiro_posicionado = ""
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

def posicionarPecas(codPeca,posPeca,horientacao):
    elem = ""
    i = 0
    linhaPeca = posPeca[0]
    colPeca = int(posPeca[1])
    if horientacao=="H":
        if codPeca == 1:
            while i<4:
                elem+=(linhaPeca+str(colPeca)+",1")
                i+=1
                colPeca+=1
            elementos = elem
        elif codPeca == 2:
            while i<5:
                elem+=(linhaPeca+str(colPeca)+",1")
                i+=1
                colPeca+=1
            elementos = elem
        elif codPeca == 3:
            linhaPeca = posPeca[0]
            colPeca= int(posPeca[1])
            elementos = (linhaPeca+str(colPeca)+",1")
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
                elem+=(col[colLetra]+str(colPeca)+",1")
                i+=1
                colLetra+=1
            elementos = elem
        elif codPeca == 2:
            while i<5:
                elem += (col[colLetra] + str(colPeca) + ",1")
                i += 1
                colLetra += 1
            elementos = elem
        elif codPeca == 3:
            elementos = (col[colLetra] + str(colPeca) + ",1")
        elif codPeca == 4:
            while i<2:
                elem += (col[colLetra] + str(colPeca) + ",1")
                i += 1
                colLetra += 1
            elementos = elem
    return elementos

encouracado1_j1 = (posicionarPecas(1,"A5","V"))
encouracad2_j1 = (posicionarPecas(1,"A5","V"))
porta_avioes1_j1 = (posicionarPecas(2,"A5","V"))
porta_avioes2_j1 = (posicionarPecas(2,"A5","V"))
submarino1_j1 = (posicionarPecas(3,"A5","V"))
submarino2_j1 = (posicionarPecas(3,"A5","V"))
submarino3_j1 = (posicionarPecas(3,"A5","V"))
submarino4_j1 = (posicionarPecas(3,"A5","V"))
submarino5_j1 = (posicionarPecas(3,"A5","V"))
cruzador1_j1 = (posicionarPecas(4,"A5","V"))
cruzador2_j1 = (posicionarPecas(4,"A5","V"))
cruzador3_j1 = (posicionarPecas(4,"A5","V"))
cruzador4_j1 = (posicionarPecas(4,"A5","V"))

encouracado1_j2 = (posicionarPecas(1,"A5","V"))
encouracad2_j2 = (posicionarPecas(1,"A5","V"))
porta_avioes1_j2 = (posicionarPecas(2,"A5","V"))
porta_avioes2_j2 = (posicionarPecas(2,"A5","V"))
submarino1_j2 = (posicionarPecas(3,"A5","V"))
submarino2_j2 = (posicionarPecas(3,"A5","V"))
submarino3_j2 = (posicionarPecas(3,"A5","V"))
submarino4_j2 = (posicionarPecas(3,"A5","V"))
submarino5_j2 = (posicionarPecas(3,"A5","V"))
cruzador1_j2 = (posicionarPecas(4,"A5","V"))
cruzador2_j2 = (posicionarPecas(4,"A5","V"))
cruzador3_j2 = (posicionarPecas(4,"A5","V"))
cruzador4_j2 = (posicionarPecas(4,"A5","V"))
print(posicionarPecas(2,"A5","H"))
print(posicionarPecas(3,"A5","H"))
print(posicionarPecas(4,"A5","H"))
jogada_j1 = arq1[5].split(";")
jogada_j2 = arq2[5].split(";")
j1.append(jogada_j1)
j2.append(jogada_j2)
print(j1)
print(j2)







