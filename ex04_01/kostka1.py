"""
Program symuluje pojedynczy rzut kostką
"""
import random

# randint(a, b) zwraca pseudolosową wartość N, taką że: a <= N <= b
rzut = random.randint(1, 6)

print('Liczba wyrzuconych oczek:', rzut)
