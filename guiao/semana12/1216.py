s = input("Qual frase tu quer inverter ?\n")
b = ""

for i in range(0, len(s)):
    b += (s[(len(s) - 1) - i])

print(b)
