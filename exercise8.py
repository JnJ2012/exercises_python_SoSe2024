def vokon_zählen(text):
    vokale = 0
    konsonanten = 0
    vokal_set = set("aeiouäöü")
    for char in text.lower():
        if char.isalpha():
            if char in vokal_set:
                vokale += 1
            else:
                konsonanten += 1
    print(f"Es gibt {vokale} Vokale und {konsonanten} Konsonaten")
vokon_zählen("Berlin")
vokon_zählen("HI,%// BerliÄN!")                                 