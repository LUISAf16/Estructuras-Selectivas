""""
Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico determina
si una persona tiene anemia o no. Lo cual depende de su nivel de hemoglobina en la sangre, de su edad
y de su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde
se determina su resultado como positivo y en caso contrario como negativo
"""
# Definir una función para determinar si una persona tiene anemia
def verificar_anemia(edad, sexo, nivel_hemoglobina):
    # Determinar el rango de hemoglobina según la edad y el sexo
    if 0 <= edad <= 1/12:  # 0 a 1 mes
        rango_min = 13
        rango_max = 26
    elif 1/12 < edad <= 6/12:  # >1 a 6 meses
        rango_min = 10
        rango_max = 18
    elif 6/12 < edad <= 12/12:  # >6 a 12 meses
        rango_min = 11
        rango_max = 15
    elif 1 < edad <= 5:  # >1 a 5 años
        rango_min = 11.5
        rango_max = 15
    elif 5 < edad <= 10:  # >5 a 10 años
        rango_min = 12.6
        rango_max = 15.5
    elif 10 < edad <= 15:  # >10 a 15 años
        rango_min = 13
        rango_max = 15.5
    elif sexo == "mujer" and edad > 15:  # mujeres > 15 años
        rango_min = 12
        rango_max = 16
    elif sexo == "hombre" and edad > 15:  # hombres > 15 años
        rango_min = 14
        rango_max = 18
    else:
        return "Datos no válidos"

    # Verificar si el nivel de hemoglobina está dentro del rango
    if nivel_hemoglobina < rango_min:
        return "Resultado positivo: La persona tiene anemia."
    else:
        return "Resultado negativo: La persona no tiene anemia."

# Ejemplo de uso del programa
edad = float(input("Ingrese la edad en años: "))
sexo = input("Ingrese el sexo (hombre/mujer): ").lower()
nivel_hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))

resultado = verificar_anemia(edad, sexo, nivel_hemoglobina)
print(resultado)
