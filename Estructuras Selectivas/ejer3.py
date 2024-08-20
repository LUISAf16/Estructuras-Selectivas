""""
Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de bolsos. 
La empresa, dependiendo del monto total de la compra, decidirá que hacer para pagar al fabricante 
Si el monto total de la compra excede de 500.000 la empresa tendrá la capacidad de invertir de su propio dinero
un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagara solicitando un credito
al fabricante Si el monto total de la compra no excede de 500.000 la empresa tendrá la capacidad de invertir
de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante. El fabricante cobra
por concepto de intereses un 20% sobre la cantidad que se le pague a crédito. 
Imprimir el valor invertido de su propio dinero, el valor prestado al banco, 
y el valor del crédito solicitado al fabricante, según sea el caso
"""
# Definir el monto total de la compra
montoTotal = 600000  # Monto total de la compra en pesos

# Verificar si el monto total excede de 500.000
if montoTotal > 500000:
    # Caso en que el monto total excede 500.000
    # La empresa invierte el 55% de su propio dinero
    inversionPropia = montoTotal * 0.55
    # La empresa pide prestado al banco el 30%
    prestamoBanco = montoTotal * 0.30
    # El resto se paga solicitando un crédito al fabricante
    creditoFabricante = montoTotal - (inversionPropia + prestamoBanco)
else:
    # Caso en que el monto total no excede 500.000
    # La empresa invierte el 70% de su propio dinero
    inversionPropia = montoTotal * 0.70
    # El resto se paga solicitando un crédito al fabricante
    creditoFabricante = montoTotal * 0.30
    # No se pide prestado al banco, por lo tanto, el préstamo es 0
    prestamoBanco = 0

# Calcular los intereses sobre el crédito al fabricante
interesesCredito = creditoFabricante * 0.20

# Imprimir los resultados
print(f"Valor invertido de su propio dinero: ${inversionPropia:.2f}")
print(f"Valor prestado al banco: ${prestamoBanco:.2f}")
print(f"Valor del crédito solicitado al fabricante: ${creditoFabricante:.2f}")
print(f"Intereses sobre el crédito al fabricante: ${interesesCredito:.2f}")
