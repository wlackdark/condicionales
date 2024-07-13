print("Este programa pide el año actual y un año cualquiera y calcula cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año " )
nombre=input("Por favor ingrese su nombre: ")
anio_actual=int (input("Ingrese el año actual: "))
anio_cualquiera=int (input("Ingrese un año cualquiera: "))
if anio_cualquiera<anio_actual:
    print(f"{nombre} han pasado {anio_actual - anio_cualquiera} años")
elif anio_cualquiera>anio_actual:
    print(f"{nombre} faltan {anio_cualquiera - anio_actual} años")
elif anio_cualquiera==anio_actual:
    print(f"{nombre} los años son iguales")

