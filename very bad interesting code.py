# THIRD TIME'S A CHARM

"""
first line: 4 positive integers < 1000,
each represents distance between consecutive cities

i'th integer = city i and i+1
"""

distances = input()
dlist = distances.split(" ")



print(f"0 {dlist[0]} {int(dlist[0]) + int(dlist[1])} {int(dlist[0]) + int(dlist[1]) + int(dlist[2])} {int(dlist[0]) + int(dlist[1]) + int(dlist[2]) + int(dlist[3])}")
print(f"{dlist[0]} 0 {int(dlist[1])} {int(dlist[1]) + int(dlist[2])} {int(dlist[1]) + int(dlist[2]) + int(dlist[3])}")
print(f"{int(dlist[0]) + int(dlist[1])} {int(dlist[1])} 0 {int(dlist[2])} {int(dlist[2]) + int(dlist[3])}")
print(f"{int(dlist[0]) + int(dlist[1]) + int(dlist[2])} {int(dlist[1]) + int(dlist[2])} {int(dlist[2])} 0 {int(dlist[3])}")
print(f"{int(dlist[0]) + int(dlist[1]) + int(dlist[2]) + int(dlist[3])} {int(dlist[1]) + int(dlist[2]) + int(dlist[3])} {int(dlist[2]) + int(dlist[3])} {dlist[3]} 0")