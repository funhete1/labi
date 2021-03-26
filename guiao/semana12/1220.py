from funcao import words_count

characters, words, lines = 0, 0, 0

f = open("1220.txt", "r")

for linha in f:
    characters+= len(linha)
    words += words_count(linha)
    lines+=1

f.close()

print("Caracteres = ",characters)
print("Palavras   = ", int(words))
print("linhas     = ", lines)
