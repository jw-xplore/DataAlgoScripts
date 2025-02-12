import time

def stacks(word):
    counter = 0
    word = word.replace(" ","")
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word.lower()
    wordArray = [0] * len(word)
    correct = True
    #makes an array of the letters
    for i in word:
        wordArray[counter] = i
        counter= counter + 1
    #makes a copy of the array as its easy to copy over (and would be faster than making a stack normally)
    listUp = wordArray

    #fills array back to front
    for j in reversed(range(len(wordArray))):
        listUp[j] = wordArray[j]
    
    #makes a reverse array which length and count being the same at the start, but count decreases meaning both arrays can be traversed at once
    listDown = [0] * len(word)
    length = len(listUp)-1
    count = length
    for j in reversed(range(len(wordArray))):
        listDown[j] = listUp[length-count]
        count = count - 1
  
    print(listDown)

   #checks both arrays from the end
    for j in range(len(wordArray)):
        if listUp[j] != listDown[j]:
            correct = False
            print(correct)
            break
        
    print(correct)
    return correct


def stackQueue(word):
    counter = 0
    word = word.replace(" ","")
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word.lower()
    wordArray = [0] * len(word)
    correct = True
    #makes an array of the letters
    for i in word:
        wordArray[counter] = i
        counter= counter + 1
    #makes a copy of the array as its easy to copy over (and would be faster than making a stack normally)
    listStack = wordArray
    listQueue = wordArray

    #fills array back to front for stack
    for j in reversed(range(len(wordArray))):
        listStack[j] = wordArray[j]


    #fills array back to front for queue
    for j in reversed(range(len(wordArray))):
        listQueue[j] = wordArray[j]


    #makes a reverse array which length and count being the same at the start, but count decreases meaning both arrays can be traversed at once
    length = len(listStack)-1
    count = length
    for j in reversed(range(len(wordArray))):
        if listStack[j] != listQueue[length-count]:
            correct = False
            print(correct)
            break
        count = count - 1
        
    print(correct)
    return correct



print('enter word:')
x = input()
start_time = time.time()
stacks(x)
time1 = time.time()
print("stack only time is : " , time1-start_time)


start_time2 = time.time()
stackQueue(x)
time2 = time.time()
print("stack and queue time is : " , time2-start_time2)






