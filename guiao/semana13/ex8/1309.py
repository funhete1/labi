from Crypto.Cipher import AES
from Crypto.Hash import SHA
import sys
import os

iname = sys.argv[1]
k = sys.argv[2]

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
if (os.path.getsize(iname)%16 != 0):
    print("File is no encrypted by AES")
    sys.exit()

if len(k) < 16:
    h = SHA.new()
    h.update(k.encode('utf-8'))
    k = h.hexdigest()
    
k = k[0:16]

f = open(iname, "r")

texto = f.read()

cipher = AES.new(k)
os.write(1, cipher.decrypt(texto))
