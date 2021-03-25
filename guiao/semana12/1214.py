counter = 0

frase = input("Qual a frase meu bom: ")

for i in range(0, len(frase)):
    if(frase[i].isdigit()):
        counter+=1

print("Quantidade de numeros: %d" % (counter))

