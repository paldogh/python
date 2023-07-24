# Programa para sumar números positivos 
 #usando el ciclo while
suma = 0
numero = float(input("Ingrese un número positivo (o un número negativo para terminar): "))

while numero >= 0:
    suma += numero
    numero = float(input("Ingrese otro número positivo (o un número negativo para terminar): "))

print("La suma de los números positivos ingresados es:", suma)
