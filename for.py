# Programa para calcular la suma de los primeros "n" 
 #números naturales usando el ciclo for

n = int(input("Ingrese un número entero positivo: "))
suma = 0

for numero in range(1, n + 1):
    suma += numero

print("La suma de los primeros", n, "números naturales es:", suma)
