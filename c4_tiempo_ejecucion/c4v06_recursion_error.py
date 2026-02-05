def calcular_factorial_recursivo(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * calcular_factorial_recursivo(numero-1)


print(calcular_factorial_recursivo(5))

import sys
print(sys.getrecursionlimit())

try:
    print(calcular_factorial_recursivo(1000))
except RecursionError as e:
    print("El número es muy grande, no se puede calcular el factorial")
