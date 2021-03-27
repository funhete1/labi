frase = ""

while True:
    a = input("fala tu o dos adalbertos: ")
    if(a == ""):
        break
    frase += a

frase = frase.replace("r", "").replace("R", "").replace("l","u").replace("L", "U")
print(frase)