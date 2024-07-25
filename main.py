def factorial(n):
    saida = 1
    for i in range(1,n + 1,1):
        saida *= i
    return saida
def fibonacci(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def gen_fibonacci(n):
    saida = [0,1,1]
    for i in range(3,n ):
        saida.append(saida[i-1] + saida[i-2])
    return saida