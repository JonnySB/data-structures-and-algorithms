def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def pyramid(n):
    if n == 1:
        return 1
    return n + pyramid(n-1)

print(factorial(5))

