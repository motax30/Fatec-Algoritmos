"""Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso
Deve-se implementar uma validação para a entrada de dados do usuário, limitando a entrada a 99, e caso outro número
fora da faixa seja informado, apresente uma mensagem informative perguntando se ele deseja informar um novo número
ou finalizar o programa."""
extenso1 = ["Zero","Um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez",
           "Onze","Doze","Treze","Quatorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove"]
extDezenas = ["Vinte","Trinta","Quarenta","Cinquenta","Sessenta","Setenta","Oitenta","Noventa"]
num = int(input("Informe um número para mostrá-lo por extenso"))
if num<0:
    print("Você digitou um número inválido. Deve-se digitar um número de 0 à 99")
elif num<=19:
    print("O número %d por extenso: %s"%(num,extenso1[num]))
elif num<=99:
    print("O número %d por extenso: %s e %s" %(num,extDezenas[(int(num/10)-2)],extenso1[(num%10)]))
