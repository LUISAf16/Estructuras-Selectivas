""""
En un supermercado se hace una promoción, mediante la cuál el cliente obtiene un descuento dependiendo 
de un color que se escoge al azar. Si el color de la balota es rojo el descuento es del 15% sobre el total 
de la compra, si la boleta es verde el descuento del 20%. Si el color es diferente a los indicados no obtendrá 
descuento. Imprimir el valor de la compra, el color de la balota, el descuento y el valor a pagar
"""
import random

# Definir el total de la compra
totalCompra = 200  # Valor total de la compra antes del descuento

# Definir los posibles colores de las balotas
colores = ["rojo", "verde", "otro"]

# Seleccionar al azar el color de la balota
colorSeleccionado = random.choice(colores)

# Determinar el porcentaje de descuento según el color de la balota
if colorSeleccionado == "rojo":
    descuento = 0.15  # Descuento del 15% si la balota es roja
elif colorSeleccionado == "verde":
    descuento = 0.20  # Descuento del 20% si la balota es verde
else:
    descuento = 0.00  # No hay descuento si la balota es de otro color

# Calcular el valor del descuento
valorDescuento = totalCompra * descuento

# Calcular el total a pagar después de aplicar el descuento
valor_a_pagar = totalCompra - valorDescuento

# Imprimir los resultados
print(f"Valor de la compra: ${totalCompra:.2f}")
print(f"Color de la balota seleccionada: {colorSeleccionado}")
print(f"Valor del descuento: ${valorDescuento:.2f}")
print(f"Valor a pagar: ${valor_a_pagar:.2f}")
