def buchstabe_ändern2(string, buchstabe):
    vokale = "aeioou"
    def buchstabe_ersetzen(x,y,z):
        x_list = list(x.lower())
        for i in range (len(x_list)):
            if x_list[i] == y:
                x_list[i] = z
        return "".join (x_list)
    for v in vokale: 
        print(buchstabe_ersetzen(x = string, y = buchstabe, z = v), end = " ")
buchstabe_ändern2(string = "banana", buchstabe = "a")


import numpy as np

a = np.arange(1, 13)
a_3d = a.reshape ((3,2,2))
print (a_3d)

print(a_3d.ndim)
print(a_3d.shape)
print(a_3d.size)

my_array = np.array([1,2,3], dtype = np.float64)
print(my_array)
