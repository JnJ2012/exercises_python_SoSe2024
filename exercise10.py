import numpy as np

d = np.arange (1, 11)

D = np.tile(d, (10, 1))

summe_zeilen = np.sum(D, axis = 1)

mittelwert_spalten = np.mean(D, axis = 0)

print(D)
print(summe_zeilen)
print(mittelwert_spalten)