# Para 1: Metodo burbuja  
import time
import random

# Define la cantidad de numeros que lleva el arreglo y luego se define que el tiempo se tome cuando se inicie la acción 
cantidad = 1500
inicio = time.time()

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Genera una lista de números aleatorios entre 1 y 2000
lista = random.sample(range(1, 2001), cantidad)

# Para lista desordenada se imprime cadena de texto, la lista y luego se define e imprime el tiempo que tardó en realizar la acción 
print("Lista desordenada:")
print(lista)
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")

# Para lista ordenada se usa bubble_sort(lista) para ordenar los datos y luego de eso se imprime la cadena de texto y lista para finalizar definiendo e imprimiendo el tiempo que tomó realizar la acción
bubble_sort(lista)
print("Lista ordenada")
print(lista )
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")


# Para 2: Metodo selección
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

# Para 3: Metodo inserción
import time
import random

cantidad = 1500
inicio = time.time()    

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

lista = random.sample(range(1, 2001), cantidad)

print("Lista desordenada:")
print(lista)    
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")

insertion_sort(lista)
print("Lista ordenada")
print(lista)
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")

# Para 4: Metodo mezcla
import time
import random

cantidad = 1500
inicio = time.time()

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

lista = random.sample(range(1, 2001), cantidad)

print("Lista desordenada:")
print(lista)
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")

merge_sort(lista)
print("Lista ordenada")
print(lista)
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")

# Para 5: Metodo rápido
import time
import random

cantidad = 1500
inicio = time.time()

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
lista = random.sample(range(1, 2001), cantidad)

print("Lista desordenada:")
print(lista)
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")

lista = quick_sort(lista)
print("Lista ordenada")
print(lista)
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")

# Para 6: Metodo heap sort
import time
import random

cantidad = 1500
inicio = time.time()

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

lista = random.sample(range(1, 2001), cantidad)

print("Lista desordenada:")
print(lista)
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")

heap_sort(lista)
print("Lista ordenada")
print(lista)
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")

cantidad = 1500
original = random.sample(range(1, 2001), cantidad)  # misma lista base para todos

# Diccionario con los nombres y funciones
metodos = {
    "Burbuja": bubble_sort,
    "Selección": selection_sort,
    "Inserción": insertion_sort,
    "Mezcla": merge_sort,
    "Rápido": quick_sort,
    "Heap": heap_sort
}

tiempos = {}

for nombre, metodo in metodos.items():
    lista = original.copy()  # copia la lista para no modificar la original
    inicio = time.time()

    # Quick sort devuelve una nueva lista, los demás modifican en sitio
    if nombre == "Rápido":
        lista = metodo(lista)
    else:
        metodo(lista)

    fin = time.time()
    tiempos[nombre] = fin - inicio
    print(f"{nombre} completado en {tiempos[nombre]:.6f} segundos")

# Resultados

print("\n")
for nombre, t in sorted(tiempos.items(), key=lambda x: x[1]):
    print(f"{nombre:10}: {t:.6f} segundos")

mejor = min(tiempos, key=tiempos.get)
print(f"\n El método más rápido fue: {mejor} ({tiempos[mejor]:.6f} segundos)")
