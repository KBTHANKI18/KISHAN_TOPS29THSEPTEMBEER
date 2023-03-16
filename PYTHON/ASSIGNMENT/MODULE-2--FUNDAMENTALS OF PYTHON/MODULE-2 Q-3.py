# Write a Python program to get the Fibonacci series of given range.

def fibonacci_series(range_num):
    a, b = 0, 1
    fib_series = []
    while b <= range_num:
        fib_series.append(b)
        a, b = b, a + b
    return fib_series