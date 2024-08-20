""""
Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico;
la formula que se aplica es: 
Cuando el sexo es femenino : num. pulsaciones = (220 - edad)/10 
Y si el sexo es masculino : num. pulsaciones = (210 - edad) /10
"""
# Definir la edad y el sexo de la persona
edad = 30  # Edad de la persona
sexo = "femenino"  # Sexo de la persona ("femenino" o "masculino")

# Calcular el número de pulsaciones según el sexo
if sexo == "femenino":
    # Fórmula para mujeres
    numPulsaciones = (220 - edad) / 10
elif sexo == "masculino":
    # Fórmula para hombres
    numPulsaciones = (210 - edad) / 10
else:
    # En caso de un sexo no especificado, no se calcula
    numPulsaciones = None
    print("Sexo no reconocido. Por favor, introduzca 'femenino' o 'masculino'.")

# Mostrar el resultado si se ha calculado correctamente
if numPulsaciones is not None:
    print(f"El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es: {numPulsaciones:.2f} pulsaciones")


