from enum import Enum

class ESumType(Enum):
    ROOT = 1
    LEFT = 2
    RIGHT = 3

def largestSubListSum(list, start = 0, type: ESumType = ESumType.ROOT):

    leftSum = 0
    rightSum = 0

    # Split list
    if (len(list) > 1):
        pivot: int = int(len(list) / 2)
        # Left
        leftList = list[:pivot]
        leftRes = largestSubListSum(leftList, start, ESumType.LEFT)

        # Right
        rightList = list[pivot:]
        leftRes = largestSubListSum(rightList, start + pivot, ESumType.RIGHT)

    # Summary
    sum = 0
    for i in list:
        sum += i

    # print
    print(list, " = ", sum , " - ", start)

    # Pick return sum
    """
    if type == ESumType.ROOT or type == ESumType.RIGHT: 
        if sum < leftSum:
            sum = leftSum
    
    if type == ESumType.ROOT or type == ESumType.LEFT: 
        if sum < rightSum:
            sum = rightSum
    """

    return (sum, list, start)


numbers = [ 1, 2, -5, 500, 1, 7, -90]
res = largestSubListSum(numbers)
print("res: ", res)