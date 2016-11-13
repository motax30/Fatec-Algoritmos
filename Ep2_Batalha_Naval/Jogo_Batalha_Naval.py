import os

print("Jogo Batalha Naval")
arq1 = open("jogador1.txt",'r').readlines()
arq2 = open("jogador2.txt",'r').readlines()
arq_saida = ''
j1 = []
j2 = []

linhasArquivoSaida = []

pecasPosicionadas_j1 = ''
pecasPosicionadas_j2 = ''
col = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]

def gerarArquivoDeSaida(linhasArquivoSaida,arquivo):
    arquivo = open('arquivo_saida.txt','w')
    linhas = []
    if os.stat('arquivo_saida.txt').st_size==0: #Verifica se o arquivo está vazio
        if len(linhasArquivoSaida) > 0:
            for j in range(0, len(linhasArquivoSaida)):
                linhas.append(linhasArquivoSaida[j])
            arquivo.writelines(linhas)
    else:
        conteudoArquivo = arquivo.readlines()
        for j in range(0,len(conteudoArquivo)):
            conteudoArquivo[j] = conteudoArquivo[j].replace(conteudoArquivo[j],'')
        if len(linhasArquivoSaida) > 0:
            for j in range(0, len(linhasArquivoSaida)):
                linhas.append(j)
                arquivo.writeline(linhas[j])

def preencherTabuleiroVazio(posicoes):
    for l in range(0,len(col)):
        for j in range(1, 16):
            posicoes+= col[l] + str(j) + ",0|"
    return posicoes

tabul_j1 = preencherTabuleiroVazio(pecasPosicionadas_j1)
tabul_j2 = preencherTabuleiroVazio(pecasPosicionadas_j2)

def verificarQtdMaximaPorPeca(codPeca,qtdPecasArquivo):
    pecas = {}
    pecas['encouracado'],pecas['portaAvioes'],pecas['submarinos'],pecas['cruzadores'] =2,2,5,4
    a= pecas['encouracado']
    if codPeca == 1 and qtdPecasArquivo>pecas['encouracado']: # Aqui é verificada a quantidade máxima encouraçados do Jogador
        linhasArquivoSaida.append('ERROR VALIDATION')
        gerarArquivoDeSaida(linhasArquivoSaida,arq_saida)
        exit()
    elif codPeca == 2 and qtdPecasArquivo > pecas['portaAvioes']: # Aqui é verificada a quantidade máxima de porta-aviões do Jogador
        linhasArquivoSaida.append('ERROR VALIDATION')
        gerarArquivoDeSaida(linhasArquivoSaida, arq_saida)
        exit()
    elif codPeca == 3 and qtdPecasArquivo > pecas['submarinos']: # Aqui é verificada a quantidade máxima de submarinos do Jogador
        linhasArquivoSaida.append('ERROR VALIDATION')
        gerarArquivoDeSaida(linhasArquivoSaida, arq_saida)
        exit()
    elif codPeca == 4 and qtdPecasArquivo > pecas['cruzadores']:# Aqui é verificada a quantidade máxima de cruzadores do Jogador
        linhasArquivoSaida.append('ERROR VALIDATION')
        gerarArquivoDeSaida(linhasArquivoSaida, arq_saida)
        exit()
    if len(arq1[5].split(";")[1].split("|"))>20: # Aqui é verificada a quantidade máxima de 20 torpedos do Jogador 1
        linhasArquivoSaida.append('ERROR VALIDATION')
        gerarArquivoDeSaida(linhasArquivoSaida, arq_saida)
        exit()
    elif len(arq2[5].split(";")[1].split("|"))>20: # Aqui é verificada a quantidade máxima de 20 torpedos do Jogador 2
        linhasArquivoSaida.append('ERROR VALIDATION')
        gerarArquivoDeSaida(linhasArquivoSaida, arq_saida)
        exit()

def extrairPecasDosArquivos():
    i = 0
    while i<=3:
        cod_j1 = (arq1[i].split("; "))[0].split(";")[0]
        posicao_direcao_j1 = (arq1[i].split("; "))[0].split(";")[1].replace("\n","").split("|")
        j = [cod_j1]
        for p in range(len(posicao_direcao_j1)):
            j.append(posicao_direcao_j1[p])
        j1.append(j)
        verificarQtdMaximaPorPeca(int(cod_j1),len(posicao_direcao_j1))
        cod_j2 = (arq2[i].split("; "))[0].split(";")[0]
        posicao_direcao_j2 = (arq2[i].split("; "))[0].split(";")[1].replace("\n","").split("|")
        k = [cod_j2]
        for p in range(len(posicao_direcao_j2)):
            k.append(posicao_direcao_j2[p])
        j2.append(k)
        verificarQtdMaximaPorPeca(int(cod_j1),len(posicao_direcao_j2))
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
    if len(posPeca)<=3:
        linhaPeca = posPeca[0]
        colPeca = int(posPeca[1])
    else:
        linhaPeca = posPeca[0]
        colPeca = int(posPeca[1]+posPeca[2])
    if horientacao=="0":
        elementos = (posPeca + ",1|")
    elif horientacao=="H":
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
        elif codPeca == 4:
            while i<qtd_Cruzadores:
                elem += (col[colLetra] + str(colPeca) + ",1|")
                i += 1
                colLetra += 1
            elementos = elem

    return elementos

unidadesDaPeca_j1 = []
unidadesDaPeca_j2 = []
def getUnidadesDaPeca(indicePeca,peca,unidadesDaPeca):
    tmp = []
    y = 0
    while y<len(peca)-1:
        p = peca[y]
        tmp.append(p)
        y+=1
    unidadesDaPeca[[indicePeca].extend(tmp)]

def posicionarPecasJogador(jogador,tabuleiroVazio,unidadesDaPeca):      #Passar como parâmetro a lista das posições do Jogador: J1 ou J2
    for c in range(0,len(jogador)):
        unidadesDaPeca.append(c + 1)
        cod = getIndicePecaJogador(jogador, jogador[c][0])
        for d in range(0,len(jogador[c])-1):
            peca = getIndicePecaJogador(jogador,jogador[c][d+1])
            iPeca1=peca[0]
            iPeca2 = peca[1]
            pos = jogador[iPeca1][iPeca2].replace(' ',"")
            tamPos = len(pos)
            if tamPos>=3:
                pos = pos[len(pos)-1:]
            else:
                pos = '0'
            peca= getElementosDaPeca(int(jogador[cod[0]][cod[1]]), jogador[peca[0]][peca[1]], pos).split('|')
            getUnidadesDaPeca(d,peca,unidadesDaPeca)
            adicionarElementosPecaNoTabuleiro(peca,tabuleiroVazio,pos)

msgErroPecForaTabuleiro = []

def adicionarElementosPecaNoTabuleiro(peca,tabuleiroVazio,posicao):
    f = 0
    while f < len(peca) - 1:
        global temp_1
        global temp_2
        global msgErroPecForaTabuleiro
        velho = str(peca[f][:len(peca[f])-2]).replace(' ',"")+",0"
        novo = peca[f]
        if tabuleiroVazio is tabul_j1:
            if velho in tabul_j1:
                ''' Aqui é verificado se a peça atual já foi posicionada anteriormente, se positivo lança-se um erro'''
                if novo in temp_1:
                    linhasArquivoSaida.append('ERROR_INVALID_INPUT_FILE')
                    gerarArquivoDeSaida(linhasArquivoSaida, arq_saida)
                    exit()
                else:
                    k = temp_1.replace(velho, novo)
                    temp_1 = k
            elif posicao!=0 or posicao!="":
                setMsgErroPecaForaTabuleiro(1,velho[:-2], peca[0][:-2] + posicao)
                break
            else:
                setMsgErroPecaForaTabuleiro(1,velho[:-2], peca[0][:-2])
                break
        elif tabuleiroVazio is tabul_j2:
            if velho in tabul_j2:
                ''' Aqui é verificado se a peça atual já foi posicionada anteriormente, se positivo lança-se um erro'''
                if novo in temp_2:
                    linhasArquivoSaida.append('ERROR_INVALID_INPUT_FILE')
                    gerarArquivoDeSaida(linhasArquivoSaida, arq_saida)
                    exit()
                else:
                    k = temp_2.replace(velho, novo)
                    temp_2 = k
            elif posicao!=0 or posicao!="":
                setMsgErroPecaForaTabuleiro(2,velho[:-2], peca[0][:-2] + posicao)
                break
            else:
                setMsgErroPecaForaTabuleiro(2, velho[:-2], peca[0][:-2])
                break
        f+=1

def setMsgErroPecaForaTabuleiro(codJogador,posFora,peca):
    global msgErroPecForaTabuleiro
    msg = "Posição %s está fora dos limites do tabuleiro.Esta posição pertence à peça %s"%(posFora, peca)
    tp =[]
    tp.append(codJogador)
    tp.append(msg)
    msgErroPecForaTabuleiro.append(tp)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#Programa Principal

#Posicionamento das peças do Jogador 1
temp_1 = tabul_j1
extrairPecasDosArquivos()
posicionarPecasJogador(j1,tabul_j1,unidadesDaPeca_j1)
pecasPosicionadas_j1= temp_1

#Posicionamento das peças do Jogador 2
temp_2 = tabul_j2
posicionarPecasJogador(j2,tabul_j2,unidadesDaPeca_j2)
pecasPosicionadas_j2= temp_2

if len(msgErroPecForaTabuleiro)>0:
    for i in range(0,len(msgErroPecForaTabuleiro)):
        print("Verifique o tabuleiro do Jogador %s.%s"%(msgErroPecForaTabuleiro[i][0],msgErroPecForaTabuleiro[i][1]))
    exit()
jogadas_j1 = arq1[5].split(";")[1].split("|")
jogadas_j2 = arq2[5].split(";")[1].split("|")

def efetuarJogada(jogada,pecasPosicionadas):
    if jogada not in pecasPosicionadas:
        linhasArquivoSaida.append('ERROR_INVALID_COORDINATE')
        gerarArquivoDeSaida(linhasArquivoSaida, arq_saida)
        exit()
    else:
        if pecasPosicionadas.find(jogada)==True:
            print('teste')

for u in range(0,len(jogadas_j1)):
    efetuarJogada(jogadas_j1[u],pecasPosicionadas_j1)


#--------------------------------------------------------------------------------------------------------------------------------------------------------

'''TESTES FUNCIONAMENTO NORMAL DO PROGRAMA'''
print("Peças posicionadas do Jogador 1: %s"%pecasPosicionadas_j1)
print("Peças posicionadas do Jogador 2: %s"%pecasPosicionadas_j2)
print("Unidade da Peça do Jogador 1: %s"%unidadesDaPeca_j1)
print("Unidade da Peça do Jogador 2: %s"%unidadesDaPeca_j2)
print("Tamanho da Lista de Unidade da Peça do Jogador 1: %s"%len(unidadesDaPeca_j1))
print("Tamanho da Lista de Unidade da Peça do Jogador 2: %s"%len(unidadesDaPeca_j2))
print(msgErroPecForaTabuleiro)

def verificarPosicoesPreenchidasnoTabuleiro(posicaoPreenchida,tabuleiroDoJogador):
    b=0
    result = ''
    while b<len(posicaoPreenchida):
        if posicaoPreenchida[b]in tabuleiroDoJogador:
            result = True
        else:
            result = False
            break
        b += 1
    return result

if verificarPosicoesPreenchidasnoTabuleiro(pecasPosicionadas_j1,tabul_j1)==True:
    print("Teste Resultado: Todas as peças estão posicionadas corretamente! Pode continuar no jogo")
else:
    print("Estão faltando posicionamentos a serem preenchidos no Tabuleiro ")

'''FIM DOS TESTES'''