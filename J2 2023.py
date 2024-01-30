# QUESTION 2

"""
notes:
Ron cooks chili
SHU:
Poblano: + 1500
Mirasol + 6000
serrano + 15500
Cayenne + 40000
Thai + 75000
Habanero + 125000

"""
import time
#start_time = time.time()

spices = {"Poblano":1500, "Mirasol":6000, 'Serrano':15500, 'Cayenne':40000, 'Thai':75000, 'Habanero':125000}

ans = 0

for i in range(int(input())):
    ans += spices[input()]

print(ans)