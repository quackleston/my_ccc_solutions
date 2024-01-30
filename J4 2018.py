""""
PROBLEM J4/S2: SUNFLOWERS

PROBLEM DESCRIPTION:
Barbara plants N different sunflowers, each with a unique height, ordered from smallest to largest,
and records their heights for N consecutive days. Each day, all of her flowers grow taller than they
were the day before.
She records each of these measurements in a table, with one row for each plant, with the first row
recording the shortest sunflower’s growth and the last row recording the tallest sunflower’s growth.
The leftmost column is the first measurement for each sunflower, and the rightmost column is the
last measurement for each sunflower.
If a sunflower was smaller than another when initially planted, it remains smaller for every measurement.
Unfortunately, her children may have altered her measurements by rotating her table by a multiple
of 90 degrees.
Your job is to help Barbara determine her original data.

INPUT SPECIFICATION:
The first line of input contains the number N (2 ≤ N ≤ 100). The next N lines each contain
N positive integers, each of which is at most 109
. It is guaranteed that the input grid represents a
rotated version of Barbara’s grid.

OUTPUT SPECIFICATION:
Output Barbara’s original data, consisting of N lines, each of which contain N positive integers.
"""""

flowers = []

n = int(input())

for i in range(n):
    flowers.append([])
    data = input()
    num = data.split()
    for j in num:
        flowers[i].append(int(j))

# int()
print(flowers)

def rotateR(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j == (len(a)-1)/2:
                a[i][j] = a[j][i]
            elif i > j:
                a[i][j] = a[2][i]
            else:
                a[i][j] = a[0][i]


    print(a)
    # a[0][0] = a[2][0]
    # a[0][1] = a[1][0]
    # a[0][2] = a[0][0]
    #
    # a[1][0] = a[2][1]
    # a[1][1] = a[1][1]
    # a[1][2] = a[0][1]
    #
    # a[2][0] = a[2][2]
    # a[2][1] = a[1][2]
    # a[2][2] = a[0][2]

rotateR(flowers)

# rotation thingy: if rotate and no work, rotate again
def rotations():
    pass


# ' '.join(str(flowers).split())

