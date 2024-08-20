""""
En una llantera se ha establecido una promoción de las llantas marca "Todo Terreno" , dicha promoción consiste 
en lo siguiente: Si se compran menos de cinco llantas el precio es de 300.000 cada una, de 250.000
si se compran de 5 a 10 y de 200.000 si se compran más de 10.
Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las llantas que compre
"""
# Definir la cantidad de llantas compradas
cantidadLlantas = 7  # Cantidad de llantas que se desean comprar

# Determinar el precio por llanta según la cantidad comprada
if cantidadLlantas < 5:
    precio_por_llanta = 300000  # Precio por llanta si se compran menos de 5
elif 5 <= cantidadLlantas <= 10:
    precio_por_llanta = 250000  # Precio por llanta si se compran entre 5 y 10
else:
    precio_por_llanta = 200000  # Precio por llanta si se compran más de 10

# Calcular el total a pagar
total_a_pagar = precio_por_llanta * cantidadLlantas

# Mostrar el precio por llanta y el total a pagar
print(f"Precio por llanta: ${precio_por_llanta:,}")
print(f"Total a pagar por {cantidadLlantas} llantas: ${total_a_pagar:,}")
