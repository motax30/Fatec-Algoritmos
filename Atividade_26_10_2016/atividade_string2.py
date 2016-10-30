# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios extras

# G. verbing
# Dada uma string, caso seu comprimento seja pelo menos 3,
# adiciona 'ing' no final
# Caso a string já termine em 'ing', acrescentará 'ly'.
def verbing(s):
    saida = ""
    if "ing" in s:
        saida = s + "ly"
    elif len(s) >= 3:
        saida = s + "ing"
    else:
        saida = s
    return saida


# H. not_bad
# Dada uma string, procura a primeira ocorrência de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'
def not_bad(s):
    n, b = s.find("not"), s.find("bad")
    z = 0
    if n > 0:
        if b > 0:
            if b > n:
                z = s.replace(s[n:b + 3], "good")
            else:
                z = s
        else:
            z = s
    return z


# I. inicio_final
# Divida cada string em dois pedaços.
# Se a string tiver um número ímpar de caracteres
# o primeiro pedaço terá um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
#  a-inicio + b-inicio + a-final + b-final
def inicio_final(a, b):
    inicio = ""
    final = ""
    x = 0
    tam_a = len(a)
    tam_b = len(b)
    ind_a = int(tam_a / 2)
    ind_b = int(tam_b / 2)
    saida = str
    if tam_a>1:
        if tam_a%2==0:
            inicio+=a[:ind_a]
            final+=a[ind_a:]
        else:
            inicio += a[:ind_a + 1]
            final += a[ind_a+1:]
        if tam_b > 1:
            if tam_b % 2 == 0:
                inicio += b[:ind_b]
                final += b[ind_b:]
            else:
                inicio += b[:ind_b + 1]
                final += b[ind_b+1:]
        else:
            saida = a + b
    else:
        saida = a + b
    saida = inicio+final
    return saida

# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três
def zf(n):
    num = str(n)
    ind = -1
    cont = 0
    x=0
    while x==0:
        if num[ind]=="0":
            cont+=1
            ind-=1
        else:
            x+=1
    return cont

# K. conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19
def conta2(n):
    x=0
    cont = 0
    while x<n:
        num = str(x)
        num_vezes = num.count("2")
        if num_vezes>0:
            cont+=num_vezes
        x+=1
    return cont

# L. inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536
def inip2(n):
    i = 0
    while True:
        tam_n = len(str(n))
        pot_2 = str(2**i)
        if pot_2.find(str(n))==0:
            break
        i+=1
    return i


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))


def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('inicio_final')
    test(inicio_final('abcd', 'xy'), 'abxcdy')
    test(inicio_final('abcde', 'xyz'), 'abcxydez')
    test(inicio_final('Kitten', 'Donut'), 'KitDontenut')

    print()
    print('zeros finais')
    test(zf(10100100010000), 4)
    test(zf(90000000000000000010), 1)

    print()
    print('conta 2')
    test(conta2(20), 2)
    test(conta2(999), 300)
    test(conta2(555), 216)

    print()
    print('inicio p2')
    test(inip2(7), 46)
    test(inip2(133), 316)
    test(inip2(1024), 10)


if __name__ == '__main__':
    main()
