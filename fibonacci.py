# Pedro Guimarães Caninas

"""

Criar  uma  função  em  sua  linguagem  preferida.  A  função  deve  receber  um  número  N  >=  0  (deve 
validar  o  input  para  a  função),  e  retornar  o  valor  correspondente  deste  número  na  sequência 
Fibonacci. EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.

-- Criar uma função recursiva que resolva Fibonacci 
-- Criar uma função iterativa que resolva Fibonacci

"""


def fibonacciRecursivaAuxiliar(N: int, F0: int, F1: int) -> int:
    if N == 0:
        return F1
    
    return fibonacciRecursivaAuxiliar(N-1, F1, F0 + F1)

def fibonacciRecursiva(N: int) -> int:
    if type(N) == int and N >= 0:
        if N == 0:
            return 0
        if N == 1 or N == 2:
            return 1

        return fibonacciRecursivaAuxiliar(N-2, 1, 1)
    
    return -1
    
def fibonacciIterativa(N: int) -> int:
    if type(N) == int and N >= 0:
        F0 = 1
        F1 = 1
        aux = 0

        if N == 0:
            return 0
        if N == 1 or N == 2:
            return 1
        
        for _ in range(2, N):
            aux = F1
            F1 += F0 
            F0 = aux

        return F1
    
    return -1

    
print("Recursivo(0):", fibonacciRecursiva(0))
print("Recursivo(1):", fibonacciRecursiva(1))
print("Recursivo(2):", fibonacciRecursiva(2))
print("Recursivo(3):", fibonacciRecursiva(3))
print("Recursivo(5):", fibonacciRecursiva(5))
print("Recursivo(6):", fibonacciRecursiva(6))

print("")

print("Iterativo(0):", fibonacciRecursiva(0))
print("Iterativo(1):", fibonacciRecursiva(1))
print("Iterativo(2):", fibonacciRecursiva(2))
print("Iterativo(3):", fibonacciRecursiva(3))
print("Iterativo(5):", fibonacciRecursiva(5))
print("Iterativo(6):", fibonacciRecursiva(6))

