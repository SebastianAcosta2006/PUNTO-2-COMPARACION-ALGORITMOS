import time
import random


def ll1_parse(input_string):
    stack = ['$', 'S']
    input_string += '$'
    i = 0

    table = {
        ('S', 'a'): ['a', 'S', 'b'],
        ('S', 'b'): [],
        ('S', '$'): []
    }

    while stack:
        top = stack.pop()
        current = input_string[i]

        if top == current:
            i += 1
        elif (top, current) in table:
            production = table[(top, current)]
            for symbol in reversed(production):
                stack.append(symbol)
        else:
            return False

    return True


# Generador de cadenas
def generar_cadena(n):
    return ''.join(random.choice(['a', 'b']) for _ in range(n))



print("LL(1) - Medición de tiempos")
print("Tamaño\tTiempo (s)")
print("-" * 25)

tamanos = [5, 10, 15, 20, 25, 50, 100]

for n in tamanos:
    cadena = generar_cadena(n)

    inicio = time.time()
    ll1_parse(cadena)
    fin = time.time()

    print(f"{n}\t{(fin - inicio):.6f}")