from funcao import words_count
import os.path
import sys


fname = "1220.txt"

if not os.path.exists(fname):
    sys.exit("Não existe")
if os.path.isdir(fname):
    sys.exit("É diretório")
if not os.path.isfile(fname):
    sys.exit("Não é ficheiro")

characters, words, lines = 0, 0, 0

f = open(fname, "r")

for linha in f:
    characters+= len(linha)
    words += words_count(linha)
    lines+=1

f.close()

print("Caracteres = ",characters)
print("Palavras   = ", int(words))
print("linhas     = ", lines)
