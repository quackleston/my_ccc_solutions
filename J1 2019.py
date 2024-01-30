# QUESTION 1

"""
notes:
first 3 lines: scoring of apples
next 3: bananas

each team:
first line: 3-pointers
second: 2-pointers
third: 1-pointers
each num between 0,100 inclusive

"""
import time

lest = []

for i in range(6):
    fruit = int(input())
    lest.append(fruit)


start_time = time.time()

applesScore = lest[0]*3 + lest[1]*2 + lest[2]*1
bananasScore = lest[3]*3 + lest[4]*2 + lest[5]*1

if applesScore > bananasScore:
    print("A")
elif bananasScore > applesScore:
    print("B")
else:
    print("T")

print("my program took", time.time() - start_time, "to run :)")