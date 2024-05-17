def buchstaben_zählen(text):
    anzahl_buchstaben = 0
    for char in text:
        if char.isalpha():
            anzahl_buchstaben += 1
    return anzahl_buchstaben
print(buchstaben_zählen("Hallo, Berlin"))
print(buchstaben_zählen("Hallo, Berlin&/§&§"))


def buchstaben_zählen2(wort):
    liste = list(wort)
    buchstaben = [i for i in liste if i.isalpha()]
    print(len(buchstaben))
    
buchstaben_zählen2("Berlin; Hallo222")