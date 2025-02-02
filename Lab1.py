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
# Singly linked list functions
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


#----------------------------------------
# Sorting
#----------------------------------------

# Sort linked list segment
def linkedListSortSegment(head: Link, compared: Link, parent: Link, position: int):
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
                    startLink.link = compared

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

# Linked list insertion sort
def linkedListInsertionSort(head: Link):
    link = head
    parent = None
    i = 0

    print("Sorting----------------------")

    while link != None:
        if i > 0:
            linksTuple = linkedListSortSegment(head, link, parent, i)
            head = linksTuple[0]
            link = linksTuple[1]
            iterateLinkedList(head)

        # Progress single level iteration
        parent = link
        link = link.link
        i += 1

    return head


# Test list 
#singleLinkedList = createLinkedList(1, 3, 5, 7, 9, 8)
singleLinkedList = createLinkedList(9, 8, 7, 3, 4, 84, 41, 6, 3, 1, 2)
iterateLinkedList(singleLinkedList)
singleLinkedList = linkedListInsertionSort(singleLinkedList)
iterateLinkedList(singleLinkedList)

