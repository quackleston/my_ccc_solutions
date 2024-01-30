allAuctions = []

bidN = int(input())

# 2

# Name
# bid

# Name
# bid

# Name
# bid


for i in range(bidN):
    bidderName = input()
    bidderPrice = int(input())
    allAuctions.append([bidderName, bidderPrice])
    # sublist so each 1st = 0, each 2nd = 1 for every one :)

highestBid = 0
highestBidder = " "

# a= [["apple","banana"],["dorito","cheeto"]]
# for i in a = ["apple","banana"], ["dorito","cheeto"]

for i in allAuctions:
    if i[1] > highestBid:
        highestBid = i[1]
        highestBidder = i[0]

print(highestBidder)
# first line: how many bids, so times 2
# because name and bid is connected
# after, a name, a bid connected to that name, etc etc
