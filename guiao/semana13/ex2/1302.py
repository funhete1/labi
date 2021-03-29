import hashlib
import sys
import os

h = hashlib.sha1()

entext = ""
iname = sys.argv[1]
out = sys.argv[2]

if not os.path.exists(iname):
    sys.exit("Não existe")
    exit
if os.path.isdir(iname):
    sys.exit("É diretório")
    exit
if not os.path.isfile(iname):
    sys.exit("Não é ficheiro")
    exit
if (os.stat(iname).st_size == 0):
    print("File is empty!")
    sys.exit()

if not os.path.exists(out):
    sys.exit("Não existe")
    exit
if os.path.isdir(out):
    sys.exit("É diretório")
    exit
if not os.path.isfile(out):
    sys.exit("Não é ficheiro")
    exit

f = open(iname, "rb")
entext = f.read(512)
while len(entext) != 0:
    h.update(entext)
    entext = f.read(512)
f.close()

f = open(out, "w")
f.write(h.hexdigest())
f.close()
