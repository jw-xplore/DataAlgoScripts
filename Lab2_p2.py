import random

#----------------------------------------
# Descrition
#----------------------------------------

"""
Program run steps:
- Call function providing list of numbers 
- Function call is self with sub list 
- Left side from 0 to half size 
- Right side from half size to end 
- Call itself until provided sub list has only 1 item 
- Return value of this one item 
- Sum all left and right numbers 
- Gain largest result at left side 
    - Compare left largest value from left (including all negative numbers from left side) to left summary + right largest value from left 
    - Pick bigger number 
- Gain largest result at right side 
    - Compare right largest value from right (including all negative numbers from right side) to right summary + left largest value from left 
    - Pick bigger number 
- Pick largest value from Sum, Largest left or Largest right results
- Return tuple with containing Sum, Largest left, Largest right and Largest value
    - These result are then used when comparing results of larger (next in recursion) sub list
    - Largest value is then used as result
    - Base case of recursion is when sublist has only 1 element. In that case tuple return value of the number for every of four values.


Time complexity:
Worst time complexity is O(n). Algorithm divides list down to single element and only combines results of tuple from left side with right side.
For each call there are following comparisons done:
- largest left results compared to left sum + right largest left result
- largest right results compared to right sum + left largest right result
- two comparisons to compare sum of left right largest result to right left largest result, with left largest sum and right largest sum

So in the end there are 4 comparision to 7 different results (
    overal sum
    left largest
    right largest
    largest of sum
    overal sum + right side left largest
    overal sum + left side right largest
    left side right largest + right side left largest
    )
"""

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