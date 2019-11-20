#P6 E1 - JOSE MIGUEL RIVAS MENDEZ - DAM - PROGRAMACIÓN
#Escribe un programa que te pida palabras y las guarde en una lista.
#Para terminar de introducir palabras, simplemente pulsa Enter.
#El programa termina escribiendo la lista de palabras.
palabra=input("Escribe una palabra: ")
lista=[]
while (palabra!=""):
    lista.append(palabra)
    palabra=input("Escribe más palabras: ")
print("Las palabras que has escrito son: ",lista)

