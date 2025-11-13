# Iterative Fibonacci with step counter

def fib_iterative(n):
    steps = 0
    if n == 0:
        steps += 1
        return 0, steps
    elif n == 1:
        steps += 1
        return 1, steps
    
    a, b = 0, 1
    for i in range(2, n + 1):
        steps += 1
        a, b = b, a + b
    return b, steps

n = int(input("Enter n: "))
result, steps = fib_iterative(n)
print(f"Fibonacci({n}) = {result}")
print(f"Step count (iterative) = {steps}")




# Recursive Fibonacci with step counter

steps = 0  # global step counter

def fib_recursive(n):
    global steps
    steps += 1  # count each call as a step
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

n = int(input("Enter n: "))
steps = 0
result = fib_recursive(n)
print(f"Fibonacci({n}) = {result}")

print(f"Step count (recursive) = {steps}")
