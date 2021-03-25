ano = int(input("Qual o ano o genio: "))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0): 
    print("Sim")
else:
    print("Nao")