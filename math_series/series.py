# Function for nth Fibonacci number
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(3))


def lucas(n):
    # declaring base values
    # for positions 0 and 1
    a = 2
    b = 1
    if (n == 0):
        return a
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


# n = 9
print(lucas(9))

