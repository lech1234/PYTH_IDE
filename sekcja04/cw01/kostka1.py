"""
Moduł symuluje pojedynczy rzut kostką.

W rozwiązaniu użyta została funkcja 'randint' z modułu 'random'.
"""
import random

if __name__ == '__main__':

    # Funkcja randint(a, b) zwraca pseudolosową wartość N, taką że: a <= N <= b
    rzut = random.randint(1, 6)

    print('Liczba wyrzuconych oczek wynosi:', rzut)
