def factorial(n):
    nu1 = n
    nu2 = 1
    for i in range (1,nu1 + 1, 1):
        nu2 *= i
    return (nu2)

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:   
        return fibonacci(n-1) + fibonacci(n-2)

def gen_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b