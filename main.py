def factorial(n):
    if n == 0:
        return 0
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gen_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = a + b, b