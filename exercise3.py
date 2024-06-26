def steigung_funktion(Punkt):
    x1 = Punkt[0]
    y1 = Punkt[1]
    x2 = Punkt[2]
    y2 = Punkt[3]
    
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    steigung = delta_y / delta_x
    
    if delta_x == 0:
        print("Die Steigung ist nicht definiert")
    else: 
        print("Die Steigung ist:", steigung)

steigung_funktion([1, 3, 8, 1])
        

städte = ["Rome", "Paris", "London", "Berlin"]
print(städte)
städte.remove("Berlin")
print(städte)
städte.append("Madrid")
print(städte)
städte.insert(1, "Amsterdam")
print(städte)
städte.sort()
print(städte)
städte.sort(reverse = True)
print(städte)