"""""
Calcular el total a pagar por la compra de zapatillas. Si se compran tres o más zapatillas 
se aplica un descuento del 20% sobre el total de la compra y si son menos de tres zapatillas un descuento
del 10%. Mostrar en pantalla el valor de la compra, el valor del descuento y el valor a pagar una vez aplicado
el descuento
"""
# Definir el precio de una zapatilla y la cantidad comprada
precioZapatilla = 50  # Precio por unidad de zapatillas
cantidadZapatillas = 4  # Cantidad de zapatillas compradas

# Calcular el valor total de la compra sin aplicar el descuento
valorCompra = precioZapatilla * cantidadZapatillas

# Determinar el porcentaje de descuento según la cantidad de zapatillas compradas
if cantidadZapatillas >= 3:
    # Si se compran tres o más zapatillas, se aplica un descuento del 20%
    descuento = 0.20
else:
    # Si se compran menos de tres zapatillas, se aplica un descuento del 10%
    descuento = 0.10

# Calcular el valor del descuento en dinero
valorDescuento = valorCompra * descuento

# Calcular el total a pagar después de aplicar el descuento
valor_a_pagar = valorCompra - valorDescuento

# Mostrar en pantalla el valor de la compra, el valor del descuento y el valor a pagar
print(f"Valor de la compra: ${valorCompra:.2f}")
print(f"Valor del descuento: ${valorDescuento:.2f}")
print(f"Valor a pagar: ${valor_a_pagar:.2f}")
