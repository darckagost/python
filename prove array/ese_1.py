# 1.Crea un array di numeri interi e calcola la somma di tutti gli elementi.
import array as arr

v=arr.array("i",[1, 20, 30, 50])


# utils
def print_value(x):
    print(f"Il risultato è: {x}")


v = arr.array("i", [1, 20, 30, 50])
"""
        __summary__: sum of array's elements.
        __return__: sum.
"""


def somma_tot():
    tot = 0
    for i in range(0, len(v)):
        tot += v[i]
    return tot


print_value(somma_tot())