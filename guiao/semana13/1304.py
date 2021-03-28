from Crypto.Cipher import ARC4
from Crypto.Cipher import SHA
import sys
import os

h = hashlib.sha1()


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

if not os.path.exists(out):
    sys.exit("Não existe")
    exit
if os.path.isdir(out):
    sys.exit("É diretório")
    exit
if not os.path.isfile(out):
    sys.exit("Não é ficheiro")
    exit

if len(k) < 5:
    h = SHA.new()
    h.update(k.encode('utf-8'))
    chave = h.hexdigest()
elif len(k) > 256:
    chave = chave[0:256]

f = open(iname, "rb")

texto = f.read()

cipher = ARC4.new(k)
cryptogram = cipher.encrypt(texto)
os.write(1, crypto)

decipher = ARC4.new(k)
decrypted = decipher.decrypt(cryptogram)

f.close()

