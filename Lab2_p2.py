
operation = 0

def largestSubListSum(list, start = 0):

    leftRes = None
    rightRes = None
    lenL = len(list)
    pivot: int = int(lenL / 2)

    # Split list
    if (lenL > 1):
        # Left
        leftList = list[:pivot]
        leftRes = largestSubListSum(leftList, start)

        # Right
        rightList = list[pivot:]
        rightRes = largestSubListSum(rightList, start + pivot)

    # Sum
    sum = 0
    if lenL == 1:
        sum = list[0]
    else:
        # Get largest left value
        leftLargestSum = 0
        leftLargestSumTemp = 0
        for i in range(pivot - 1, -1, -1):
            leftLargestSumTemp += list[i]
            if leftLargestSumTemp > leftLargestSum:
                leftLargestSum = leftLargestSumTemp
        
        print("largest left: ", leftLargestSum)

        rightLargestSum = 0
        rightLargestSumTemp = 0
        for i in range(pivot, lenL, 1):
            rightLargestSumTemp += list[i]
            if rightLargestSumTemp > rightLargestSum:
                rightLargestSum = rightLargestSumTemp

        print("largest right: ", rightLargestSum)

        # Get only positive or sum
        if leftLargestSum > 0 and rightLargestSum > 0: # sum
            sum = leftLargestSum + rightLargestSum
        elif leftLargestSum > 0 and rightLargestSum < 0: # left
            sum = leftLargestSum
        elif leftLargestSum < 0 and rightLargestSum > 0: # right
            sum = rightLargestSum
        else:
            sum = 0 # none

        sum = leftLargestSum + rightLargestSum

    print("sum of ", list, "is: ", sum)

    return sum


numbers = [ -1, 2, -3, 4, 5, -4, 8]
res = largestSubListSum(numbers)
print("res: ", res)