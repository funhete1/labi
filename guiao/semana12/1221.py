from funcao import reverse
import os.path
import sys


fname = "1221.txt"

if not os.path.exists(fname):
    sys.exit("Não existe")
if os.path.isdir(fname):
    sys.exit("É diretório")
if not os.path.isfile(fname):
    sys.exit("Não é ficheiro")

f = open(fname,"r")

for linha in f:
    print(reverse(linha)) #da merda se tiver mais linhas no txt

f.close()