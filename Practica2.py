import math

entrada = input("Ingrese una muestra de números separados por comas: ")

numeros = [float(numero) for numero in entrada.split(',')]

media = sum(numeros) / len(numeros)

suma_cuadrados_diferencias = sum((numero - media) ** 2 for numero in numeros)

desviacion_tipica = math.sqrt(suma_cuadrados_diferencias / len(numeros))

print("La media de la muestra es:", media)
print("La desviación típica de la muestra es:", desviacion_tipica)






