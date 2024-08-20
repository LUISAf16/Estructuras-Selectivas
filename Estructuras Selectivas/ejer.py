
"""""
determinar si un aprendiz aprueba o desaprueba algoritmia, sabiendo que aprobara si su promedio
de tres calificaciones es mayor o igual a  7; reprueba en caso contrario
"""
# Definir las tres calificaciones del aprendiz
calificacion1 = 85  # Primera calificación
calificacion2 = 75  # Segunda calificación
calificacion3 = 60  # Tercera calificación

# Calcular el promedio de las tres calificaciones
promedio = (calificacion1 + calificacion2 + calificacion3) / 3

# Verificar si el promedio es mayor o igual a 70
if promedio >= 70:
    # Si el promedio es mayor o igual a 70, el aprendiz aprueba
  print("El aprendiz aprueba.")
else:
    # Si el promedio es menor que 70, el aprendiz reprueba
    print("El aprendiz reprueba.")
