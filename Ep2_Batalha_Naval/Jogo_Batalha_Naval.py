print("Jogo Batalha Naval")
arq1 = open('jogador1.txt','r').readlines()
arq2 = open('jogador2.txt','r').readlines()
j1 = []
j2 = []
i=0
tabuleiro = ""
col = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]

while i<=3:
    cod_j1 = (arq1[i].split("; "))[0].split(";")[0]
    posicao_direcao_j1 = (arq1[i].split("; "))[0].split(";")[1].replace("\n","")
    j = [cod_j1,posicao_direcao_j1]
    j1.append(j)
    cod_j2 = (arq2[i].split("; "))[0].split(";")[0]
    posicao_direcao_j2 = (arq2[i].split("; "))[0].split(";")[1].replace("\n", "")
    l = [cod_j1, posicao_direcao_j2]
    j2.append(l)
    i+=1
jogada_j1 = arq1[5].split(";")
jogada_j2 = arq2[5].split(";")
j1.append(jogada_j1)
j2.append(jogada_j2)
print(j1)
print(j2)

#def verificarPosicaoPecaSobreposta(cod_peca,posicao):
 #   if cod_peca==1:
