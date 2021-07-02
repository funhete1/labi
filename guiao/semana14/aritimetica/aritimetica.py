def sume(a, b): 
    return round(a+b)

def subtraction(a, b):
    return round(a-b)

def multiplication(a, b):
    return (a*b)

def division(a, b):
    assert b != 0 , "can't divide by zero"
    return  round((a/b), 2)

def rest(a, b):
    return a%b

def sqrt(a):
    assert a > 0 , "only real numbers"
    return pow(a, 1/2)
