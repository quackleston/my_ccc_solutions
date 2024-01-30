
C = int(input())

one = input().split(" ")
two = input().split(" ")

total = 0

# check same horizontal
for i in range(len(one)-1):
    if one[i] == "1":
        if one[i+1] == "1" or one[i-1] == "1":
            total += 2
        else:
            total += 3
        if one[i] == two[i]:
            total += 2

    if two[i] == "1":
        if two[i+1] == "1" or two[i-1] == "1":
            total += 2
        else:
            total += 3


print(total)

### output is 0

#
# check same vertical
#
# check if two adjacent same lane, then count how many then 3n-(n-1)??
# check if horizontal too
#
'''
BRIE'S CODE

C = int(input())

one = input().split(" ")
two = input().split(" ")

total = 0

# Calculate tape for the first row
for i in range(C):
    if one[i] == "1":
        # Base perimeter for a single tile
        total += 3

        # Check for adjacent wet tiles in the same row
        if (i > 0 and one[i - 1] == "1") or (i < C - 1 and one[i + 1] == "1"):
            total -= 1

        # Check for vertically adjacent wet tile
        if two[i] == "1":
            total -= 1

# Calculate tape for the second row
for i in range(C):
    if two[i] == "1":
        # Base perimeter for a single tile
        total += 3

        # Check for adjacent wet tiles in the same row
        if (i > 0 and two[i - 1] == "1") or (i < C - 1 and two[i + 1] == "1"):
            total -= 1

        # This check is not needed as it's already done in the first row loop
        # if one[i] == "1":
        #     total -= 1

print(total)
'''
