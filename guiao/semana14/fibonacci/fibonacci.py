def fibonacci(n):
    f = [10]
    if n < 0:
       return []
    elif n == 0:
        f[n] = 0
        return f
    else:
        for i in range(0, n):
            f[i] = fibonacci(i-1) + fibonacci(i-2)
        return f