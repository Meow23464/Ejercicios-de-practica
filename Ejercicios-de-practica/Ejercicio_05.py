# Pedir los datos necesarios 
X = float(input("Introduce el valor de X: "))
Y = float(input("Introduce el valor de Y: "))

if Y != 0:
    R = X / (2 * Y)
    print(f"El resultado de la expresión R = X / (2 * Y) es: {R}")
else:
    print("La expresión no se puede calcular porque Y es igual a 0 (división por cero).")
