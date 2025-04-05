import numpy as np

def ordenar_ascendente(arreglo):
    """Ordena un arreglo en orden ascendente (similar a sort())"""
    if isinstance(arreglo, np.ndarray):
        # Para numpy arrays
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n-i-1):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        return arreglo
    elif isinstance(arreglo, list):
        # Para listas de Python
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n-i-1):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        return arreglo
    else:
        raise TypeError("Tipo de arreglo no soportado")

def ordenar_descendente(arreglo):
    """Ordena un arreglo en orden descendente (similar a reverse() después de sort())"""
    if isinstance(arreglo, np.ndarray):
        # Para numpy arrays
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n-i-1):
                if arreglo[j] < arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        return arreglo
    elif isinstance(arreglo, list):
        # Para listas de Python
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n-i-1):
                if arreglo[j] < arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        return arreglo
    else:
        raise TypeError("Tipo de arreglo no soportado")