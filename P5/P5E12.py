#P5 E12 - JOSE MIGUEL RIVAS MENDEZ - DAM - PROGRAMACIÓN
#Escribe un programa que pida un número y escriba si primo o no:
numero=int(input("Dame un número: "))
resto=1
for i in range(numero):
       if ((i!=0)and(i!=1)and(numero%i==0)):
              resto=0
if (resto==0):
       print("El número ",numero,"no es primo")
else:
       print("El número ",numero,"es primo")

