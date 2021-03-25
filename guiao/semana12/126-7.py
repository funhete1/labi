pratododia = ["batata", "cenoura", "arroz", "feijao", "frango"]
dieta = [["salada"], ["salada"]]
extra = ["farofa"]

print(pratododia[0:5])

dieta[0].extend(pratododia)
extra.extend(pratododia)

print(dieta[0])
print(extra)

dieta[1].append("pao")
dieta[1].append("quejo")
dieta[1].append("carne")
dieta[1].append("bacon")
dieta[1].append("molho especial")
dieta[1].append("batata")

print(sorted(dieta[1])) #aparentemente por default organiza por ordem alfabetica
