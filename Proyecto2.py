#Ordenación_de_Arreglo_Multidimensional

#Importar_función_de_ordenación
from typing import List

# Definir una matriz bidimensional de 3x3 con valores numéricos
matrix = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Función para ordenar una fila específica de la matriz en orden ascendente (Bubble Sort)
def ordenar_fila_ascendente(matriz: List[List[int]], fila: int):
    matriz[fila] = sorted(matriz[fila])

# Mostrar la matriz original
print("Matriz Original:")
for fila in matrix:
    print(fila)

# Ordenar la segunda fila de la matriz en orden ascendente
ordenar_fila_ascendente(matrix, 1)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con Fila Ordenada:")
for fila in matrix:
    print(fila)
