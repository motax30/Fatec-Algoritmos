
def preencherTabuleiroVazio():
    col = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
    posicoes = ''
    for l in range(0,len(col)):
        for j in range(1, 16):
            posicoes+= col[l] + str(j) + ",0|"
    return posicoes

def extrairPecaDoArquivo(arquivo):
    i = 0
    lista = []
    while i<=3:
        cod_j1 = (arquivo[i].split("; "))[0].split(";")[0]
        posicao_direcao_j1 = (arquivo[i].split("; "))[0].split(";")[1].replace("\n","").split("|")
        item = [cod_j1]
        for p in range(len(posicao_direcao_j1)):
            item.append(posicao_direcao_j1[p])
        lista.append(item)
        i += 1
    return lista


