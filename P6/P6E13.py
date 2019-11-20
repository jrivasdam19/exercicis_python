#P6 E13 - JOSE MIGUEL RIVAS MENDEZ - DAM - PROGRAMACIÓN
#Desarrolla de nuevo el ejercicio de la práctica anterior
#de los números primos, con while. Reflexiona y escribe en
#el propio programa en forma de comentario, qué opción es mejor y por qué.
"""numero=int(input("Dame un número: "))
resto=1
for i in range(numero):
       if ((i!=0)and(i!=1)and(numero%i==0)):
              resto=0
if (resto==0):
       print("El número ",numero,"no es primo")
else:
       print("El número ",numero,"es primo")"""
numero=int(input("Dame un número: "))
resto=1
mod=1
while(resto!=0):
    mod+=1
    resto=numero%mod
if (mod==numero):
    print("El número",numero,"es primo")
else:
    print("El número",numero,"no es primo")

#Es mejor utilizar un while porque si el número es muy grande,
#ya diviendo entre 2 se da cuenta el programa que no es primo, mientras
#que con un for haría todas las divisiones.
