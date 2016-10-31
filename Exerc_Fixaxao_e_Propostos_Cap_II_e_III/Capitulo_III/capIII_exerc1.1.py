a = int(input("Informe os valor de a."))
b = int(input("Informe o valor de b."))
c = int(input("Informe os valor de c"))
delta = (b**2)-4*a*c
x1=(-b+((delta)**(1/2))/2*a)
x2=(-b-((delta)**(1/2))/2*a)
print("A primeira raiz é: %f e a segunda raiz é:%f"%(x1,x2))