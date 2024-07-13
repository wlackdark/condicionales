print("Pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas " )
nombre=input("Por favor ingrese su nombre: ")
veg=int (input("Para una pizza vegetariana ingresa 1 y para una pizza no vegetariana ingresa 2: "))

if veg==1:
    print(f"{nombre} has seleccionado pizza vegetariana \nLos ingredientes son: Pimiento y tofu")
elif veg==2:
    print(f"{nombre} has seleccionado pizza no vegetariana \nLos ingredientes son: Peperoni, jamón y salmón")
else:
    print(f"{nombre} has ingresado un valor incorrecto")



