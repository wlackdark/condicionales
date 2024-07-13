print("Programa que pide al usuario dos números enteros y muestra si el resultado de la multiplicación entre ambos es par o impar" )
nombre=input("Por favor ingrese su nombre: ")
num1=int (input(f"{nombre} ingrese su el primer numero: "))
num2=int (input(f"{nombre} ingrese su el segundo numero: "))
mult=num1*num2
entero=mult%2

if entero==0:
    print(f"{nombre} El resultado de la multiplicacion entre {num1} * {num2} es {mult} y es un numero par")
else:
    print(f"{nombre} El resultado de la multiplicacion entre {num1} * {num2} es {mult} y es un numero impar")
    