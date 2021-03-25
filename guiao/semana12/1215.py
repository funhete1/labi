frase = input("Diz a frase ai filhao: ")
array = []

for i in range(0, len(frase) - 1):
    array[i] = frase.split(" ")

for i in range(0, len(frase) - 1):
    print(array[i])
    