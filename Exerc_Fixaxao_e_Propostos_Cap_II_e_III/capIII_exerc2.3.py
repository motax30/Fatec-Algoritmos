print("Algoritmo cálculo da das raízes de uma equação do 2° Grau")
a = int(input("Insira o valor de a:"))
b = int(input("INsira o valor de b:"))
c = int(input("Insira o valor de c:"))
delta = b**2-4*a*c
x1 = (-b+((delta)**(1/2)))/2*a
x2 = (-b-((delta)**(1/2)))/2*a
print("O valor da primeira raiz é: %d.\n O valor da segunda raiz é: %d"%(x1,x2))