a = int(input("Insira o primeiro número:"))
b = int(input("INsira o segundo número:"))
c = int(input("Insira o terceiro número:"))
if(a<b and a<c and b<c):
    print("Sequência numérica Crescente:a-) %d,b-) %d,c-) %d"%(a,b,c))
    print("Sequência numérica Inversa:c-) %d,b-) %d,a-) %d"%(c,b,a))
elif(a<b and a<c and b>c):
    print("Sequência numérica Crescente:a-) %d,c-) %d,b-) %d" % (a,c,b))
    print("Sequência numérica Inversa:a-) %d,c-) %d,b-) %d"%(b,c,a))
elif(b<a and b<c and c<a):
    print("Sequência numérica Crescente:b-) %d,c-) %d,a-) %d"%(b,c,a))
    print("Sequência numérica Inversa:c-) %d,b-) %d,a-) %d"%(a,c,b))
elif(b<a and b<c and c>a):
    print("Sequência numérica Crescente:b-) %d,a-) %d,c-) %d"%(b,a,c))
    print("Sequência numérica Inversa:c-) %d,a-) %d,b-) %d"%(c,a,b))
elif(c<a and c<b and a<b):
    print("Sequência numérica Crescente:c-) %d,a-) %d,b-) %d" % (c, a, b))
    print("Sequência numérica Inversa:b-) %d,a-) %d,c-) %d" % (b, a, c))
elif(c<a and c<b and a>b):
    print("Sequência numérica Crescente:c-) %d,b-) %d,a-) %d" % (c, b, a))
    print("Sequência numérica Inversa:a-) %d,b-) %d,c-) %d" % (a, b, c))
