def function_1(x):
    x += 20
    return x

def function_2(w):
    w += function_1(w)
    return w

def function_3(c):
    c += function_2(c)
    return c

def function_4(b):
    b += function_3(b)
    return b


def main():
    a = 100
    total = function_4(a)
    print(total)

main()