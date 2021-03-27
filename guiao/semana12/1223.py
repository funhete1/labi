ap1 = float(input("Nota do AP1: "))
proj1 = float(input("Nota do primeiro projeto: "))
tt1 = float(input("Nota do primeiro teste teorico: "))
ap2 = float(input("Nota do AP2: "))
proj2 = float(input("Nota do segundo projeto: "))
tt2 = float(input("Nota do segundo teste teorico: "))

nf = 0.1*ap1 + 0.15*proj1 + 0.2*tt1 + 0.1*ap2 + 0.25*proj2 + 0.2*tt2

print("Aprovado") if nf >= 9.5 else print("reprovado") 