print ("Hola, este es un programa que verifica la declaración de la renta")
nombre=input("Por favor ingrese su nombre ")
salario=int(input(f" {nombre} ingrese el valor del salario"))
if salario>=0 and salario<10000:
    print(f" {nombre} Su declaracion de renta es: {salario*0.05}")
elif salario >= 10000 and salario<20000:
    print(f"{nombre} Su declaracion de renta es: {salario*0.15}")
elif salario >= 20000 and salario<35000:
    print(f"{nombre} Su declaracion de renta es: {salario*0.20}")
elif salario >= 35000 and salario<60000:
    print(f"{nombre} Su declaracion de renta es: {salario*0.30}")
elif salario >= 60000:
    print(f"{nombre} Su declaracion de renta es: {salario*0.45}")
else:
    print(f"{nombre} No es un salario correcto")
