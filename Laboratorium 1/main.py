import math


import numpy as np


def cylinder_area(r: float, h: float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if h < 0 or r < 0:
        return np.NaN
    else:
        return 2 * math.pi * r**2 + 2 * math.pi * r * h

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    if n > 0 and type(n) is int:
        if n == 1:
            lst = [1]
            vec = np.array(lst)
            return vec
        elif n == 2:
            lst = [1, 1]
            vec = np.array(lst)
            return vec
        else:
            lst = [1, 1]
            for x in range(2, n):
                lst.append(lst[x-1]+lst[x-2])
            vec = np.array(lst)
            return np.array([vec])
    return None


def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    a = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    det = np.linalg.det(a)
    t = np.transpose(a)
    if det != 0:
        inv = np.linalg.inv(a)
    else:
        inv = np.NaN
    return (inv, t, det)

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if type(n) is int and type(m) is int and m > 0 and n > 0:
        a = np.zeros(shape=(m, n))
        for i in range(m):              # przechodze po wierszach, jest ich m
            for j in range(n):          # przechodze po kolumnach, jest ich n
                if i > j:
                    a[i][j] = i
                else:
                    a[i][j] = j
        return a
    return None