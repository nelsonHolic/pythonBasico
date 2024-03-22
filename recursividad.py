import time

def print_list_while(l: list):
    i = 0
    while i < len(l):
        print(l[i])
        i += 1


print_list_while(list(range(10)))

def print_list(l: list, i: int = 0):
    if i < len(l):
        print(l[i])
        print_list(l, i + 1)

print("with recursivity ---------------------------")
print_list(list(range(10)))

def fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)

begin = time.time()
print(f"fibonacci(35)={fibonacci(35)}")
print(f"it takes = {time.time() - begin}")

fibonaccis: dict[int, int] = {}

def fibonacci_with_memory(n: int):
    if n in fibonaccis:
        return fibonaccis[n]
    if n == 0:
        return 0
    if n == 1:
        return 1

    result = fibonacci_with_memory(n - 2) + fibonacci_with_memory(n - 1)
    fibonaccis[n] = result
    return result

begin = time.time()
print(f"with cache memory, fibonacci(35)={fibonacci_with_memory(35)}")
print(f"it takes = {time.time() - begin}")

def factorial(n: int):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(f"factorial(10) = {factorial(10)}")


