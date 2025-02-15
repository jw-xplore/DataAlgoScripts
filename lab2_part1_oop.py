import time

class Stack:
    
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
    
    def pop(self):
        pos = len(self.data) - 1
        value = self.data[pos]
        self.data.pop(pos)
        return value
    
class Queue:
     
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
    
    def pop(self):
        value = self.data[0]
        self.data.pop(0)
        return value

def stacks(word):

    word = word.replace(" ","")
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word.lower()

    #makes a copy of the array as its easy to copy over (and would be faster than making a stack normally)
    listUp = Stack()

    #fills array back to front
    for j in word:
        listUp.push(j)

    print(listUp.data)
    
    #makes a reverse array which length and count being the same at the start, but count decreases meaning both arrays can be traversed at once
    listDown = Stack()

    for j in reversed(range(len(word))):
        listDown.push(word[j])
  
    print(listDown.data)

    #checks both arrays from the end
    for j in range(len(word)):

        popUpVal = listUp.pop()
        popDowVal = listDown.pop()
        print("first stack pop: " , popUpVal)
        print("second stack pop: " , popDowVal)

        #fail to data are not same
        if popUpVal != popDowVal:
            print("Word is not palindrome")
            return False
        
    #success
    print("Word is palindrome")
    return True


def stackQueue(word):

    word = word.replace(" ","")
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word.lower()

    #makes a copy of the array as its easy to copy over (and would be faster than making a stack normally)
    listStack = Stack()
    listQueue = Queue()

    #fills array back to front for stack
    for j in word:
        listStack.push(j)

    #fills array back to front for queue
    for j in word:
        listQueue.push(j)


    #makes a reverse array which length and count being the same at the start, but count decreases meaning both arrays can be traversed at once
    for j in range(len(word)):

        popStackVal = listStack.pop()
        popQueueVal = listQueue.pop()

        print("stack pop: ", popStackVal)
        print("queue pop: ", popQueueVal)

        if popStackVal != popQueueVal:
            print("Word is not palindrome (Stack-Queue)")
            return False
        
    #success
    print("Word is palindrome (Stack-Queue)")
    return True



print('enter word:')
x = input()
start_time = time.time()
stacks(x)
time1 = time.time()


start_time2 = time.time()
stackQueue(x)
time2 = time.time()

print("stack only time is : " , time1-start_time)
print("stack and queue time is : " , time2-start_time2)






