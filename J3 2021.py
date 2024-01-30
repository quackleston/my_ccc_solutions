rawData = []
processedData = []

while True:
    encodedDirection = input()
    rawData.append(encodedDirection)
    if(encodedDirection == "99999"):
        break

rawData.pop()
print(rawData)

directions = " "
for i in range(len(rawData)):
    directions = rawData[i][:2]
    if((int(directions[0]) + int(directions[1])) == 0):
        processedData.append([processedData[i-1][0],rawData[i][2:]])
    elif (int(directions[0]) + int(directions[1])) % 2 == 0:
        processedData.append(["right",rawData[i][2:]])
    else:
        processedData.append(["left", rawData[i][2:]])



