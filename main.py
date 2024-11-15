import base64

def base64Sifrele(metin):
    metinBytes = metin.encode('ascii')
    base64Bytes = base64.b64encode(metinBytes)
    base64SifreliMesaj = base64Bytes.decode('ascii')
    return base64SifreliMesaj

def base64SifreCoz(sifreliMetin):
    base64Bytes = sifreliMetin.encode('ascii')
    metinBytes = base64.b64decode(base64Bytes)
    sifresizMetin = metinBytes.decode('ascii')
    return sifresizMetin

metin = input("Şifrelenmesi istenilen metin: ")
sifreliMetin = base64Sifrele(metin)
print("Şifreli Metin\n" + sifreliMetin)

sifreCozulmusMetin = base64SifreCoz(sifreliMetin)
print("Çözülen Metin\n" + sifreCozulmusMetin)
