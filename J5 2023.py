# check 1/last letter and look up down right left laskjfksjf

W = input()  # word
R = int(input())  # number of rows
C = int(input())  # number of columns
counter = 0

crossword = []

for i in range(R):
    crossword.append(input().split(" "))

# while counter != R-1:
#     for i in crossword[counter]:
#         if i == W[0] or i == W[-1]:

def checkWord(i, j, word):
    # check right
    if j + len(word) <= C and all(crossword[i][j + k] == word[k] for k in range(len(word))):
        return True
    # check down
    if i + len(word) <= R and all(crossword[i + k][j] == word[k] for k in range(len(word))):
        return True
    # check diagonal down right
    if i + len(word) <= R and j + len(word) <= C and all(crossword[i + k][j + k] == word[k] for k in range(len(word))):
        return True
    # check diagonal down right
    if i + len(word) <= R and j + len(word) <= C and all(crossword[i + k][j - k] == word[k] for k in range(len(word))):
        return True
    return False


def is_valid_position(x, y):
    # checks if given positions (x,y) are within the boundaries of the crossword
    return 0 <= x < R and 0 <= y < C


def matches_word(x, y, dx, dy, segment):
    # checks each character if the words still match with what they should be even when going in a diff direction
    # starts at (x,y) in the direction of (dx,dy)
    return all(is_valid_position(x + l * dx, y + l * dy) and crossword[x + l * dx][y + l * dy] == segment[l] for l in range(len(segment)))


def checkBentWord(i, j, word):
    # defines the directions: right, down, diagonal down-right, diagonal down-left
    directions = [(0,1), (1,0), (1,1), (1,-1)]
    """
    The directions variable in your code is a list of tuples, where each tuple represents a direction in which we can traverse the grid.
    Each tuple in the directions list is a pair of integers (dx, dy). Here's what each pair represents:

    1. (0, 1): This represents a movement to the right. Here, dx (change in the row index) is 0, meaning we stay in the same row, and dy (change in the column index) is 1, meaning we move one column to the right.

    2. (1, 0): This represents a movement downwards. Here, dx is 1, meaning we move one row down, and dy is 0, meaning we stay in the same column.

    3. (1, 1): This represents a diagonal movement down-right. Both dx and dy are 1, meaning we move one row down and one column to the right simultaneously.

    4. (1, -1): This represents a diagonal movement down-left. Here, dx is 1, meaning we move one row down, and dy is -1, meaning we move one column to the left.

    In the checkBentWord function, these directions are used to check both segments of the word (before and after the bend). The function first picks a direction from the directions list and checks if the first part of the word exists in that direction starting from the current grid position (i, j). If it does, the function then checks all possible directions for the second part of the word starting from the end of the first part.
    
    """

    # try/iterate each direction
    for dx,dy in directions:
        # try bending the words at each point (except first and last)
        for s in range(1, len(word)):
            # splits our word (ie MENU) into two parts at index s
            firstPart = word[:s]
            secondPart = word[s:]

            # check if the "first part" (non-bended part) matches with the word so far
            if matches_word(i, j, dx, dy, firstPart):
                # calculates the end position
                endX, endY = i + dx * (s - 1), j + dy * (s - 1)


for i in range(R):
    for j in range(C):
        if crossword[i][j] == W[0] or crossword[i][j] == W[-1]:
            if(checkWord(i, j, W) or checkWord(i, j, W[::-1])):
                counter += 1

print(counter)




'''
MENU
5
7
F T R U B L K
P M N A X C U
A E R C N E O
M N E U A R M
M U N E M N S
'''
