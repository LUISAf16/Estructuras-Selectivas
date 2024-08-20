""""
Se ha establecido un programa para estimular a los alumnos, el cuál consiste en lo siguiente: 
si el promedio obtenido por un alumno en el último periodo es mayor o igual que 4.0, se le hará un descuento 
del 30% sobre la pensión; si el promedio obtenido es menor que 4.0 debera pagar la pensión completa
la cual incluye el 10% del IVA. Obtener cuánto debe pagar un alumno
"""
# Definir el promedio del alumno y la pensión mensual
promedio = 3.8  # Promedio del alumno en el último periodo
pensionMensual = 1000  # Valor de la pensión mensual antes de aplicar cualquier descuento o IVA

# Calcular el monto a pagar según el promedio
if promedio >= 4.0:
    # Si el promedio es mayor o igual a 4.0, se aplica un descuento del 30%
    monto_a_pagar = pensionMensual * 0.70  # 70% de la pensión
else:
    # Si el promedio es menor que 4.0, se paga la pensión completa con IVA
    monto_a_pagar = pensionMensual * 1.10  # 100% de la pensión más 10% de IVA

# Mostrar el resultado
print(f"El alumno debe pagar: ${monto_a_pagar:.2f}")
