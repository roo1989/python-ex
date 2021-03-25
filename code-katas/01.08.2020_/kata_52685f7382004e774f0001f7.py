def fib(n):
    a, b = '0', '1'
    out = ''

    for i in range(n):
        c = a + b
        b,a = a, c
        out += c

    return out


print(fib(0),'0')
print(fib(1),'01')
print(fib(2),'010')
print(fib(3),'01001')
print(fib(5),'0100101001001')
