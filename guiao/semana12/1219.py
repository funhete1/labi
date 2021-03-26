from funcao import batata

a = int(input("qual o menor valor do intervalo: "))
b = int(input("qual o maior valor do intervalo: "))

if(a > b):
    while a > b:
        a = int(input("qual o menor valor do intervalo: "))
        b = int(input("qual o maior valor do intervalo: "))

else:
    print(batata(a, b))

