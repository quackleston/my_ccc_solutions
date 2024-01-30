"""
notes:
schedule event on 1/5 possible days
determine which day so people attend is largest
"""

d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for i in range(int(input())):
    days = input("")
    for letters in range(len(days)):
        if days[letters] == "Y":
            d[letters+1] += 1

lest = []
laest = list(d.values())

laester = max(laest)

for t in range(len(laest)):
    if laest[t] == laester:
        lest.append(str(t+1))

if(len(lest) == 1):
    print(lest[[0]])
else:
    print(','.join(lest))


