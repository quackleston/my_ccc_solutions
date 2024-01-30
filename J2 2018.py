# THE SECOND OF THE PROBLEMOS

"""
fruits = ['apple', 'banana', 'cherry', "cherry"]
listOfIndex = []

counter = 0
for i in range(len(fruits)):
    if fruits[i] == 'cherry':
        listOfIndex.append(i)

print(fruits)
print(listOfIndex)
"""

N = input()

lists = []
counter = 0

for i in range(2):
    day = input()
    lists.append(day)

print(lists)
for x in range(len(lists[0])):
    if lists[0][x] == "C" and lists[0][x] == lists[1][x]:
        counter = counter + 1

print(lists[0][0])
print(counter)
