# regular, gold, black
tarjeta = input("Ingresa tu tipo de tarjeta(regular, gold, black): ")

if tarjeta == "regular":
    print("Tienes un descuento del 2%")
elif tarjeta == "gold":
    print("Tienes un descuento del 10%")
elif tarjeta == "black":
    print("Tienes un descuento del 15%")
else:
    print("Ingresa una tarjeta válida.")