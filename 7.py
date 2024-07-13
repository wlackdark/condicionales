print("Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos. " )
nombre=input("Por favor ingrese su nombre: ")
num1=int (input("Ingrese el primer numero "))
num2=int (input("Ingrese el segundo numero "))
num3=int (input("Ingrese el tercer numero "))

if num1==num2 and num2==num3:
    print (f"{nombre} Los numeros {num1}, {num2} y {num3} son iguales")
elif num1==num2 or num1==num3 or num2==num3:
    print (f"{nombre} Los numeros {num1}, {num2} y {num3} hay dos iguales")
else:
    print (f"{nombre} Los numeros {num1}, {num2} y {num3} son todos diferentes")

   