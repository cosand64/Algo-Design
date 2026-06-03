

def fibonacci_loop(n):
    fibonacci = (n + 1) * [0]
    fibonacci[0] = 0
    fibonacci[1] = 1

    for n in range(2, n + 1):
        fibonacci[n] = fibonacci[n - 1] + fibonacci[n - 2]
    
    return fibonacci

def recursive_fibonacci(n):
    pass

def main():
    n = 100
    print(fibonacci_loop(n))

main()