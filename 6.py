print("Este programa pide dos números enteros y calcula si el mayor es múltiplo del menor " )
nombre=input("Por favor ingrese su nombre: ")
num1=int (input("Ingrese el primer numero "))
num2=int (input("Ingrese el segundo numero "))
if num1>num2:
    mod = num1 % num2
    if mod == 0:
        print (f"{nombre} el {num1} es multiplo de {num2}")
    elif mod != 0:
        print (f"{nombre} el {num1} no es multiplo de {num2}")
elif num1<num2:
    mod = num2 % num1
    if mod == 0:
        print (f"{nombre} el {num2} es multiplo de {num1}")
    elif mod != 0:
        print (f"{nombre} el {num2} no es multiplo de {num1}")
elif num1==num2:
    print (f"{nombre} el {num2} es igual a {num1} y por tanto son multiplos")

