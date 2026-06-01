def factorial_by_recursion(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_by_recursion(n-1)

def factorial_by_loop(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

def main():
    print(factorial_by_loop(10))
    print(factorial_by_recursion(10))

main()
