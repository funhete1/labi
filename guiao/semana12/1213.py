a, b, count= 0, 1, 0

while count < 10:
    print(a)
    c = a + b
    # update values
    a = b
    b = c
    count += 1