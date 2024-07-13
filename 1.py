print("Programa que clasifica segun el rango de edad de una persona \n 0 a 5 años Primera Infancia \n 6 a 11 años Infancia \n 12 a 18 años Adolescencia \n 14 a 26 años Juventud \n 27 a 59 años Adultez \n 60 o más años Persona mayor" )
nombre=input("Por favor ingrese su nombre: ")
edad=int (input(f"{nombre} ingrese su edad: "))
if edad<=5 and edad>=0:
    print(f"{nombre} usted esta en el rango Primera Infancia")
elif edad<12 and edad>=6:
    print(f"{nombre} usted esta en el rango Infancia")
elif edad<19 and edad>=12:
    print(f"{nombre} usted esta en el rango Adolescencia")
elif edad<27 and edad>=14:
    print(f"{nombre} usted esta en el rango Juventud")
elif edad<60 and edad>=27:
    print(f"{nombre} usted esta en el rango Adultez")
elif edad<130 and edad>=60:
    print(f"{nombre} usted esta en el rango Persona Mayor")
else:
    print("Esta fuera del rango de edad")