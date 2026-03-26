import time
import random

def cyk(grammar, string):
    n = len(string)
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Inicialización
    for i in range(n):
        for var, productions in grammar.items():
            for prod in productions:
                if prod == string[i]:
                    table[i][i].add(var)

    # Llenado de tabla
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for var, productions in grammar.items():
                    for prod in productions:
                        if len(prod) == 2:
                            B, C = prod
                            if B in table[i][k] and C in table[k+1][j]:
                                table[i][j].add(var)

    return 'S' in table[0][n-1]


# Gramática en CNF
grammar = {
    'S': [('A', 'B'), ('B', 'C')],
    'A': [('B', 'A'), 'a'],
    'B': [('C', 'C'), 'b'],
    'C': [('A', 'B'), 'a']
}

# Generador de cadenas
def generar_cadena(n):
    return ''.join(random.choice(['a', 'b']) for _ in range(n))



print("CYK - Medición de tiempos")
print("Tamaño\tTiempo (s)")
print("-" * 25)

tamanos = [5, 10, 15, 20, 25]

for n in tamanos:
    cadena = generar_cadena(n)

    inicio = time.time()
    cyk(grammar, cadena)
    fin = time.time()

    print(f"{n}\t{(fin - inicio):.6f}")