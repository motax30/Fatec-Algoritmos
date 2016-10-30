print("Termos da série de Fibonacci até a soma acumulada de 4000")
a,b = 0,1
todosTermos = []
par = []
impar = []
somaAcumulada = 0
somatorioPar=0
somatorioImpar=0
soma_quadrado=0
while True:
    if(a%2==0):
        somatorioPar+=a
        soma_quadrado+= a*a
        somaAcumulada+= a
        par.append(a)
        todosTermos.append(a)
        a = a+b
    elif (a%2!=0):
        somatorioImpar+= a
        soma_quadrado+=a*a
        somaAcumulada += a
        impar.append(a)
        todosTermos.append(a)
        a = a + b
    if a >= 4000:
        break
    elif(b%2==0):
        somatorioPar+=b
        soma_quadrado += b*b
        somaAcumulada += b
        par.append(b)
        todosTermos.append(b)
        b = b+a
    elif (b%2!=0):
        somatorioImpar += b
        soma_quadrado += b*b
        somaAcumulada += b
        impar.append(b)
        todosTermos.append(b)
        b = b+a
    if b >= 4000:
        break
tacm = "0"
z = 1
while z<len(todosTermos):
    termo = todosTermos[z]
    t= (str)(termo)
    tacm=tacm+"+"+t
    z+=1
print("Série Fibonacci\nO valor acumulado dos termos %s é: %d"%(tacm,somaAcumulada))

tpar = "0"
j = 1
while j<len(par):
    termo=par[j]
    t = (str)(termo)
    tpar = tpar + "+" + t
    j += 1
print("O valor da soma dos termos de ordem par %s é de: %d" %(tpar,somatorioPar))
timpar = "1"
l = 1
while l<len(impar):
    termo=impar[l]
    t = (str)(termo)
    timpar = timpar + "+" + t
    l += 1
print("O valor da soma dos termos de ordem impar %s é de: %d" %(timpar,somatorioImpar))
print("A soma dos quadrados dos termos é: %d"%soma_quadrado)