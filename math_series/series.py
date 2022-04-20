# Function for nth Fibonacci number
def fibonacci(n):
    # Declare placeholder
    # for position 2
    if n == 2:
        return 1
    elif n == 0 or n == 1:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(2))


# Function for nth Lucas number
def lucas(n):
    a = 2
    b = 1
    # declare placeholders
    # for positions 0 and 1
    if n == 0 or n == 1:
        return a
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b


print(lucas(1))

