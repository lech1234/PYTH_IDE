"""
Program symuluje pojedynczy rzut kostką
"""
import random

# składnia:
#    random.randrange(stop)
#    random.randrange(start, stop)
#    random.randrange(start, stop, step)
# domyślnie: start = 0, step = 1
# zwraca pseudolosową wartość N, taką że start <= N < stop

rzut = random.randrange(6) + 1
# lub:
# rzut = random.randrange(1, 7)

print('Liczba wyrzuconych oczek:', rzut)
