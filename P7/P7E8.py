#P7 E8 - JOSE MIGUEL RIVAS MENDEZ - DAM - PROGRAMACIÓN
#Escribe un programa que pida una frase, y pase la frase
#como parámetro a una función que debe eliminar los espacios
#en blanco (compactar la frase). El programa principal imprimirá
#por pantalla el resultado final.

def cadena(frase):
    n=0
    if frase[0]!=" ":
        aux=frase[0]
    else:
        aux=" "
    for i in range(1,len(frase)):
        if frase[i]==" ":
            aux=aux[:(i-n)]+frase[(i+1):]
            n+=1
    return aux

frase=input("Dime una frase: ")
print(cadena(frase))

"""def cadena(frase):
    
    for i in range(len(frase)):
        if frase[i]==" ":
            frase1=frase.replace(frase[i],"")
    return frase1

frase=input("Dime una frase: ")
print(cadena(frase))"""
