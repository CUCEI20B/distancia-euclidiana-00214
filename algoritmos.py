import math

def distancia_euclidiana(origen_x, origen_y, destino_x, destino_y):
    return math.sqrt((destino_x - origen_x)**2 + (destino_y - origen_y)**2)


""" Calcula la distancia euclidiana

Devuelve el resultado de la formula

También se le conoe a la fórmula como:
distancia entre dos puntos

Parámetros:
x_1 -- origen_x
y_1 -- origen_y
x_2 -- destino_x
y_2 -- destino_y

"""
    