# Definición de la función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Llamada a la función con argumentos
base_triangulo = 4
altura_triangulo = 3
area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)

# Mostrar el resultado
print("El área del triángulo es:", area_triangulo)
