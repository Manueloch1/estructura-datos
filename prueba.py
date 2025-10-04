import time
import random


cantidad = 1500
inicio = time.time()


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

lista = random.sample(range(1, 2001), cantidad)

print("Lista desordenada:")
print(lista)
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")

selection_sort(lista)
print("Lista ordenada")
print(lista)
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")