# Pedro Guimarães Caninas

"""

Criar  uma  função  em  sua  linguagem  preferida.  A  função  deve  receber  um  número  N  >  1  (validar 
o  input),  e  retornar  todos  os  números  primos  até  o  número  N.  EX.  p(2)  =  [2];  p(3)  =  [2,  3];  p(10)  =  [2, 
3, 5, 7]; 

-- Criar uma função recursiva que resolva p 
-- Criar uma função iterativa que resolva p 

"""


import math


def primo_recursivo(N: int, divisor: int, limite: int) -> bool:
    if divisor > limite:
        return True
     
    if N % divisor == 0:
        return False
    
    return primo_recursivo(N, divisor + 1, limite)

def numeros_primos_recursivo(N: int, i: int = 2) -> list[int]:
    if not isinstance(N, int) or N <= 1:
        raise ValueError("N deve ser um inteiro maior que 1")

    if i > N:
        return []

    if primo_recursivo(i, 2, math.floor(math.sqrt(i))):
        return [i] + numeros_primos_recursivo(N, i + 1)
    
    return numeros_primos_recursivo(N, i+1)


def primo_iterativo(N: int) -> bool:
    for i in range(2, math.floor(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
        
    return True
    
def numeros_primos_iterativo(N: int) -> list[int]:
    numeros_primos_ate_N = []

    if not isinstance(N, int) or N <= 1:
        raise ValueError("N deve ser um inteiro maior que 1")

    for i in range(2, N + 1):
        if primo_iterativo(i):
            numeros_primos_ate_N.append(i)

    return numeros_primos_ate_N


print("Iterativo(2):", numeros_primos_iterativo(2))
print("Recursivo(2):", numeros_primos_recursivo(2))

print("")

print("Iterativo(3):", numeros_primos_iterativo(3))
print("Recursivo(3):", numeros_primos_recursivo(3))

print("")

print("Iterativo(10):", numeros_primos_iterativo(10))
print("Recursivo(10):", numeros_primos_recursivo(10))