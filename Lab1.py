import math

#----------------------------------------
# Single linked list link class
#----------------------------------------

class Link:
    number = 0
    link = None

    def __init__(self, num):
        self.number = num

#----------------------------------------
# Single list functions
#----------------------------------------

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

# Array insertion sort
def arrayInsertionSort(list):
    for i in range(1, len(list) - 1):
        j = i
        while j > 0 and list[j - 1] > list[j]:
            num = list[j]
            list[j - 1]
            list[j] = num


            j -= 1



# Sort linked list segment
def linkedListSortSegment(head: Link, compared: Link, position: int):
    link: Link = head
    startLink: Link = head
    StartLinkI = 0
    i = 0

    middleI =  int(math.floor(position * 0.5))
    halfSize = middleI

    while link != None:

        # Stepping forward
        if halfSize == 0:
            # End
            if compared.number <= link.number:
                print("Place num: " + str(compared.number) + ", into i: " + str(i))
                break

            link = link.link
            i += 1
            continue


        # Reaching mid point
        if i == middleI:
            # Debug print
            # print(str(i) + ") pos = " + str(link.number))

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

            sub = int(math.floor(halfSize * 0.5))
            if sub < 1:
                sub = 1
            halfSize -= sub

            # End placing
            #if halfSize == 0:
                #print("Place num: " + str(compared.number) + ", into i: " + str(i))
                #break

            # Restart conting
            #link = startLink 
            #i = 0 # This should be of startlink id
            continue

        # Progress list
        link = link.link
        i += 1

# Linked list insertion sort
def linkedListInsertionSort(head: Link):
    link = head
    i = 0

    print("Sorting----------------------")

    while link != None:
        if i == 5:
            linkedListSortSegment(head, link, i)
        # Progress single level iteration
        link = link.link
        i += 1


# Test list 
singleLinkedList = createLinkedList(1, 3, 5, 7, 9, 8)
iterateLinkedList(singleLinkedList)
linkedListInsertionSort(singleLinkedList)

