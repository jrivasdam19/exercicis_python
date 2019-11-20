#P4 E1 - JOSE MIGUEL RIVAS MENDEZ - DAM - PROGRAMACIÓN
#Pida al usuario 5 números y diga cual es el mayor y cuál el menor

numero1=float(input("Introduzca el primer número "))
numero2=float(input("Introduzca el segundo número "))
numero3=float(input("Introduzca el tercero número "))
numero4=float(input("Introduzca el cuarto número "))
numero5=float(input("Introduzca el quinto número "))
if(numero1==numero2==numero3==numero4==numero5):
    print("Todos los numeros son iguales")
else:
    if(numero1>numero2):
        mayor=numero1
        menor=numero2
    else:
        mayor=numero2
        menor=numero1
    if(numero3>mayor):
        mayor=numero3
    if(numero3<menor):
        menor=numero3
    if(numero4>mayor):
        mayor=numero4
    if(numero4<menor):
        menor=numero4
    if(numero5>mayor):
        mayor=numero5
    if(numero5<menor):
        menor=numero5
    print(mayor, "es el mayor y" ,menor, "es el menor")

    
    
