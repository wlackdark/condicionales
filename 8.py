print("Programa que calcula el area de un triangulo o un circulo " )
nombre=input("Por favor ingrese su nombre: ")
seleccion= input("Ingrese c para calcular el area de un circulo o t para calular el area de un triangulo: ")
seleccion=seleccion.lower()
if seleccion == "t":
    base=int (input("Ingrese la base del traingulo "))
    altura=int (input("Ingrese la altura del traingulo "))
    print (f"{nombre} el area del triangulo es {(base*altura)/2} ")
elif seleccion =="c":
    radio=int (input("Ingrese el radio del circulo "))
    print (f"{nombre} el area del circulo es {3.14*radio**2} ")
else:
    print(f"{nombre} has ingresado un valor invalido")