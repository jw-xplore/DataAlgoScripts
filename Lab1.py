import math
import random
import time

global operations
operations = 0

#----------------------------------------
# Create testing data
#----------------------------------------

def createTestData(size: int, sorted: bool, randMin: int, randMax: int, nudgeSort = False):
    
    file = open("testData.txt", "w")
    number = random.randrange(randMin, randMax)

    for i in range(0, size):
        file.write(str(number) + "\n")

        if sorted == True:
            number += random.randrange(randMin, randMax)
        else:
            number = random.randrange(randMin, randMax)

    # Add smaller number to end to break sort
    if nudgeSort == True:
        number = number - randMax - 1
        file.write(str(number) + "\n")

    file.close()


#----------------------------------------
# Create reverse testing data
#----------------------------------------

def createReverseTestData(size: int, sorted: bool, randMin: int, randMax: int, nudgeSort = False):
    
    file = open("testData.txt", "w")
   

    for i in range(0, size):
        file.write(str(size-i)+ "\n")

     
  

    file.close()




#----------------------------------------
# Single linked list link class
#----------------------------------------

class Link:
    number = 0
    link = None

    def __init__(self, num):
        self.number = num

def createLinkedList(*params):

    head = Link(params[0])
    link = head

    for i in range(1, len(params)):
        nextLink = Link(params[i])
        link.link = nextLink
        link = nextLink

    return head

# Iterate through linked list from head 
def iterateLinkedList(head: Link):

    link = head
    i = 0

    print("Iterate:")

    while link != None:
        print(str(i) + ". num: " + str(link.number))
        link = link.link
        i += 1

def linkedListFromDocument():

    head:Link = None
    link:Link = None

    with open('testData.txt', 'r') as file:
        for line in file:
            if head == None:
                head = Link(int(line))
                link = head
            else:
                nextLink = Link(int(line))
                link.link = nextLink
                link = nextLink

    return head

#----------------------------------------
# Doubly linked list link class
#----------------------------------------

class DualLink(Link):
    link = None

    def __init__(self, num: int, parent: Link, link: Link):
        self.number = num
        self.parent = parent
        self.link = link

def createDualLinkedList(*params):

    head = DualLink(params[0], None, None)
    link = head

    for i in range(1, len(params)):
        nextLink = DualLink(params[i], link, None)
        link.link = nextLink
        link = nextLink

    return head

def iterateDualLinkedList(head: DualLink):

    link = head
    i = 0

    print("Iterate:")

    while link != None:
        num:str = "none"
        if link.parent != None:
            num = str(link.parent.number);
        
        print(str(i) + ". num: " + str(link.number) + "(" + num + ")")
        link = link.link
        i += 1

def dualLinkedListFromDocument():

    head:DualLink = None
    link:DualLink = None

    with open('testData.txt', 'r') as file:
        for line in file:
            if head == None:
                head = DualLink(int(line), None, None)
                link = head
            else:
                nextLink = DualLink(int(line), link, None)
                link.link = nextLink
                link = nextLink

    return head

#----------------------------------------
# Sorting
#----------------------------------------

# Sort linked list segment
def linkedListSortSegment(head: Link, compared: Link, parent: Link, position: int):
    link: Link = head
    startLink: Link = head
    StartLinkI = 0
    i = 0
    global operations

    middleI =  int(math.floor(position * 0.5))
    halfSize = middleI

    while link != None:
        operations = operations + 1
        # Stepping forward
        if halfSize == 0:
            # End
            if compared.number <= link.number:
                #iterateLinkedList(head)
                #print("Place num: " + str(compared.number) + ", into i: " + str(i))

                # Relink
                if i != position:
                    parent.link = compared.link
                    compared.link = link
                else:
                    parent = link

                # Change head
                if i == 0:
                    head = compared
                else:
                    if i != position:
                        startLink.link = compared

                #iterateLinkedList(head)
                # Return new head and compared number parent
                return (head, parent)

            StartLinkI = link
            link = link.link
            i += 1
            continue

        # Reaching mid point
        if i == middleI:
            # Setup starting point
            if compared.number > link.number: # Right - start point is middle link
                middleI += int(math.floor(halfSize * 0.5))
                startLink = link
                StartLinkI = i
                link = link.link
                i += 1
            else:
                middleI -= int(math.floor(halfSize * 0.5)) # Left - start point is same
                link = startLink
                i = StartLinkI

            # Shrink changing point
            sub = int(math.floor(halfSize * 0.5))
            if sub < 1:
                sub = 1
            halfSize -= sub

            continue

        # Progress list
        link = link.link
        i += 1

# Sort double linked list segment
def sortDualLinkSegment(head: DualLink, compared: DualLink, parent: DualLink, position: int):
    link: DualLink = head
    startLink: DualLink = head
    StartLinkI = 0
    i = 0
    global operations

    middleI =  int(math.floor(position * 0.5))
    halfSize = middleI

    backStep: bool = False

    while link != None:
        operations = operations + 1
        # Stepping forward
        if halfSize == 0 or i == 0:

            # End
            if compared.number <= link.number:

                # Relink
                #compared.parent = link.parent

                if i != position:
                    parent.link = compared.link
                    
                    if compared.link != None:
                        compared.link.parent = compared.parent

                    compared.parent = link.parent
                    compared.link = link

                    if compared.link != None:
                        compared.link.parent = compared
                else:
                    parent = link

                #if i != position:
                #compared.parent = link.parent

                # Change head
                if i == 0:
                    head = compared
                    link.parent = compared
                    compared.parent = None
                else:
                    if i != position:
                        startLink.link = compared
                        #link.parent.link = compared

                # Return new head and compared number parent
                return (head, parent)

            StartLinkI = link

            # Progress list
            if backStep == False:
                link = link.link
                i += 1
            else:
                link = link.parent
                i -= 1
            continue

        # Reaching mid point
        if i == middleI:
            # Setup starting point
            if compared.number > link.number: # Right - start point is middle link
                middleI += int(math.floor(halfSize * 0.5))
                startLink = link
                StartLinkI = i
                link = link.link
                i += 1
                backStep = False
            else:
                middleI -= int(math.floor(halfSize * 0.5)) # Left - start point is same
                backStep = True

            # Shrink changing point
            sub = int(math.floor(halfSize * 0.5))
            if sub < 1:
                sub = 1
            halfSize -= sub

            continue

        # Progress list
        if backStep == False:
            link = link.link
            i += 1
        else:
            link = link.parent
            i -= 1

    return

# Linked list insertion sort
def linkedListBinsertionSort(head: Link):
    link = head
    parent = None
    i = 0

    print("Sorting----------------------")

    while link != None:
        
        if i > 0:
            linksTuple: tuple

            if isinstance(link, DualLink) == False:
                linksTuple = linkedListSortSegment(head, link, parent, i) # Singly linked list sorting
            else:
                linksTuple = sortDualLinkSegment(head, link, parent, i) # Double linked list sorting

            head = linksTuple[0]
            link = linksTuple[1]

        # Progress single level iteration
        parent = link
        link = link.link
        i += 1

    return head


# Test list 

#singleLinkedList = createLinkedList(1, 3, 5, 7, 9, 8)
#singleLinkedList = createLinkedList(9, 8, 7, 3, 4, 41, 84, 6, 3, 1, 2)
#createTestData(15000, True, 1, 5)

# Generate data
createTestData(10000, False, 1, 20)

# Singly linked list
linkedList = linkedListFromDocument()

operations = 0
start_time = time.time()
linkedList = linkedListBinsertionSort(linkedList)

print("Singly linked list sort finished --- %s seconds ---" % (time.time() - start_time) + " operations = " + str(operations))


# Doubly linked list
dualLinkedList = dualLinkedListFromDocument()

operations = 0
start_time = time.time()
dualLinkedList = linkedListBinsertionSort(dualLinkedList)

print("Doubly linked list sort finished --- %s seconds ---" % (time.time() - start_time) + " operations = " + str(operations))

#iterateDualLinkedList(dualLinkedList)
