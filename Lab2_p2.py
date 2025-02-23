import random

#----------------------------------------
# Create testing data
#----------------------------------------

def createTestData(size: int, randMin: int, randMax: int):
    
    file = open("testData.txt", "w")

    for i in range(0, size):
        number = random.randrange(randMin, randMax)
        if number == 0:
            number = random.choice([randMin, randMax])

        file.write(str(number) + "\n")

    file.close()

def listFromTestData():
    list = []
    with open('testData.txt', 'r') as file:
        for line in file:
            list.append(int(line))

    return list

#----------------------------------------
# Algorithm
#----------------------------------------

def largestSubListSum(list):

    lenL = len(list)

    # Return single element result
    if lenL == 1:
        res = list[0]
        return (res, res, res, res)

    pivot: int = int(lenL / 2)

    # Left
    leftList = list[:pivot]
    leftRes = largestSubListSum(leftList)

    # Right
    rightList = list[pivot:]
    rightRes = largestSubListSum(rightList)

    # Sum results
    sum = leftRes[0] + rightRes[0]

    # Largest left most result - either left or combine left sum with largest right result
    largestLeft = leftRes[1]
    if largestLeft < (leftRes[0] + rightRes[1]):
        largestLeft = leftRes[0] + rightRes[1]
    
    # Largest right most result - either right or combine right sum with largest left result
    largestRight = rightRes[2]
    if largestRight < (leftRes[2] + rightRes[0]):
        largestRight = leftRes[2] + rightRes[0]

    # Select largest sum from combinations
    largestSum = leftRes[2] + rightRes[1]
    if largestSum < leftRes[3]:
        largestSum = leftRes[3]
    if largestSum < rightRes[3]:
        largestSum = rightRes[3]

    return (sum, largestLeft, largestRight, largestSum)


createTestData(10, -10, 10)
numbers = listFromTestData()
print("Numbers: ", numbers)
res = largestSubListSum(numbers)
print("Res: ", res[3])