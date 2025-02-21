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


numbers = [ -2, 1, -3, 4, -1, 2, 1, -5, 4]
res = largestSubListSum(numbers)
print("res: ", res[3])