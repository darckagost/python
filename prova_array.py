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

# 2. Aggiungi un elemento a un array e stampa il risultato.
v.append(7)
print_value(v)

# 3. Rimuovi un elemento da un array dato e stampa il risultato.
v.remove(7)
print_value(v)

# 4. Itera su un array e stampa solo gli elementi pari.
for i in range(0, len(v)):
    if v[i] % 2 == 0:
        print(v[i]) 