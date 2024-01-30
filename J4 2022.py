""""
something aint right...
"""""


besties = []
enemies = []
groups = []

x = int(input())
for i in range(x):
    bestie = tuple(input().split(" "))
    besties.append(bestie)

y = int(input())
for i in range(y):
    enemy = tuple(input().split(" "))
    enemies.append(enemy)

g = int(input())
for i in range(g):
    group = input().split(" ")
    groups.append(group)

"""

In the context of using sum(1 for ...) in this code, the purpose is to count occurrences where the specified conditions are met. The generator expression 1 for s1, s2, s3 in groups ... essentially creates a sequence of ones for each iteration of the loop where the conditions are satisfied. Then, the sum() function adds up all these ones, effectively counting the number of occurrences that satisfy the specified conditions.

If you use 0 instead of 1, you'll end up with sum(0 for ...), which would always sum to zero regardless of how many conditions are met. The 1 in this context acts as a counter, and by summing these ones, you get a count of occurrences.
"""

invalid = sum(
    1 for s1, s2, s3 in groups
    if (s1, s2) in enemies or (s1, s3) in enemies or (s2, s3) in enemies
    or (s1, s2) not in besties or (s1, s3) not in besties or (s2, s3) not in besties
)-1


print(invalid)


"""
[('A', 'B'), ('G', 'L'), ('J', 'K')]
[('D', 'F'), ('D', 'G')]
[['A', 'C', 'G'], ['B', 'D', 'F'], ['E', 'H', 'I'], ['J', 'K', 'L']]

3
A B
G L
J K
2
D F
D G
4
A C G
B D F
E H I
J K L

output 3


1
ELODIE CHI
0
2
DWAYNE BEN ANJALI
CHI FRANCOIS ELODIE


"""

