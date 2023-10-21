"""
Moduł symuluje pojedynczy rzut kostką.

W rozwiązaniu użyta została funkcja 'randrange' z modułu 'random'.
"""
import random

if __name__ == '__main__':

    # Składnia funkcji:
    #    random.randrange(stop)
    #    random.randrange(start, stop)
    #    random.randrange(start, stop, step)
    # domyślnie: start = 0, step = 1
    # Zwraca pseudolosową wartość N taką, że start <= N < stop

    rzut = random.randrange(6) + 1
    # lub:
    # rzut = random.randrange(1, 7)

    print('Liczba wyrzuconych oczek wynosi:', rzut)
