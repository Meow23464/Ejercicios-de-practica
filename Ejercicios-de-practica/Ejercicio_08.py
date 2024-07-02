longitud_cm = float(input("Ingrese la longitud en centímetros: "))

pulgadas = longitud_cm / 2.54
metros = longitud_cm / 100
kilometros = longitud_cm / 100000

print(f"{longitud_cm} centímetros equivalen a:")
print(f"{pulgadas:.2f} pulgadas")
print(f"{metros:.2f} metros")
print(f"{kilometros:.2f} kilómetros")
