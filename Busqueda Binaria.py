def binary_search(arr, x):
    """
    Realiza una búsqueda binaria para encontrar el elemento x en la lista ordenada arr.
    Devuelve el índice del elemento si se encuentra en la lista, o -1 si no se encuentra.
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def cargar_numeros():
    """
    Solicita al usuario que ingrese el nombre del archivo que contiene los números
    y devuelve una lista de enteros.
    """
    nombre_archivo = input("Ingrese el nombre del archivo que contiene los números: ")
    with open(nombre_archivo, "r") as f:
        numeros = [int(x) for x in f.readline().split(",")]
    return numeros

def ingresar_numeros():
    """
    Solicita al usuario que ingrese los números separados por comas y devuelve una lista de enteros.
    """
    numeros = [int(x) for x in input("Ingrese los números separados por comas: ").split(",")]
    return numeros

# Pide al usuario que seleccione si desea cargar los números desde un archivo o ingresarlos manualmente
opcion = input("Seleccione una opción:\n1) Cargar números desde un archivo.\n2) Ingresar números manualmente.\n")

# Si la opción es 1, carga los números desde un archivo
if opcion == "1":
    numeros = cargar_numeros()
# Si la opción es 2, solicita al usuario que ingrese los números manualmente
elif opcion == "2":
    numeros = ingresar_numeros()
else:
    print("Opción inválida.")
    exit()

# Ordena la lista de números
numeros.sort()

# Solicita al usuario que ingrese el número a buscar
busqueda = int(input("Ingrese el número a buscar: "))

# Realiza una búsqueda binaria en la lista de números utilizando la función binary_search
resultado = binary_search(numeros, busqueda)

# Imprime el resultado de la búsqueda
if resultado == -1:
    print(f"{busqueda} no se encuentra en la lista.")
else:
    print(f"{busqueda} se encuentra en la posición {resultado}.")

## Brandon Morales https://www.instagram.com/lewenn19/