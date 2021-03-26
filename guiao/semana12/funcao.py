def batata(a, b):
    c = 0
    while a <= b:
        if a % 3 == 0:
            c = c + 1
        a = a + 1
    return c

def words_count(frase):
    for i in range(0, len(frase)):
        c = len(frase.split(" ")) - 0.5 
    return c