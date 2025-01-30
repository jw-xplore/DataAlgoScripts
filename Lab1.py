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

# Array insertion sort
def arrayInsertionSort(list):
    for i in range(1, len(list) - 1):
        j = i
        while j > 0 and list[j - 1] > list[j]:
            num = list[j]
            list[j - 1]
            list[j] = num

            j -= 1

# Linked list insertion sort
def linkedListInsertionSort(head: Link):
    link = head
    i = 0

    while link != None:
        link = link.link
        i += 1
        j = i

        # while j > 


# Test list 
singleLinkedList = createLinkedList(5, 4, 8, 21, 14, 3, 24, 18, 45, 100, 7, 62)
iterateLinkedList(singleLinkedList)

