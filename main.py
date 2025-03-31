# class for the linked list structure, it is a doubly linked list
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# class that models a LRUCache, this is done using doubly linked list
class LRUCache:
    def __init__(self, pageFrameCount):
        self.capacity = pageFrameCount
        self.cache = {}
        # head and tail nodes are set to placeholders for easier linked list manipulation
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        # creates lists to store the page frame history, page fault history and, initialises variable to track page fault score
        self.pageFrameHistory = [[" " for i in range(15)] for i in range(4)]
        self.pageFaultHistory = []
        self.pageFaultScore = 0 

    # function that is used to remove a node from the cache - linked list
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    # function that is used to insert a value at the head of the cache - linked list
    def insertAtHead(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    # updates the cache - linked list with a page number
    def updatePage(self, key):

        # if the page number is already in the cache it is moved to the head
        if key in self.cache:
            node = self.cache[key]

            # removes node from list and replaces it at head - most recently used
            self.remove(node)
            self.insertAtHead(node)
            return node.value # returns page frame of page sequence num
        return -1 # does not exist in cache
    
    # inserts new page number into cache
    def insertNewPage(self, key, value):

        # checks if page number is already present in cache
        if key in self.cache:
            self.remove(self.cache[key])

        # after checks for page number presence are done insert the node at the head of the cache - linked list
        newNode = Node(key, value)
        self.insertAtHead(newNode)
        self.cache[key] = newNode

        # ensure the cache - linked list doesn't exceed specified capacity, default = 4
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

    def updatePageFrameHistory(self, timeStep):
        for index, (key) in enumerate(self.cache):
            self.pageFrameHistory[index][timeStep] = key

    def outputPageFrameHistory(self):
        for frame in range(len(self.pageFrameHistory)):
            cleansedFrameOuput = " ".join(map(str, self.pageFrameHistory[frame]))
            print(f"Page Frame {frame}: {cleansedFrameOuput}")

    def outputPageFaultHistory(self):
        output = " ".join(map(str, self.pageFaultHistory))
        return output
    
    def countPageFaults(self):
        self.pageFaultScore = len(self.pageFaultHistory)
        print(f"Page fault score is {self.pageFaultScore}")


# function to take user input of page number sequence
def inputPageOrder():

    pageSequence = []

    while len(pageSequence) != 15:

        pageNum = int(input("Enter a page number (0-9): "))
        pageSequence.append(pageNum)

    print("Full page sequence has been entered")
    print(pageSequence)

    return pageSequence

def memoryManagement():

    # intialises variable to hold user entered page number sequence and handles some output format logic
    pageSequence = inputPageOrder()
    outputIndent = " " * len("Page Frame 0: ")
    pageSequenceOutput = " ".join(map(str, pageSequence))

    # intialises variable with a capacity, and creates a lru cache with the specified capacity
    capacity = 4
    lru = LRUCache(capacity)

    # displays the process of the page frames being filled over 15 timesteps
    for timeStep in range(len(pageSequence)):
        pageNumStr = str(pageSequence[timeStep])
        pageStr = "Page " + pageNumStr

        if lru.updatePage(pageNumStr) == -1:
            lru.insertNewPage(pageNumStr, pageStr)
            lru.pageFaultHistory.append("*")
        
        lru.updatePageFrameHistory(timeStep)
        print(f"{outputIndent}     The paging sequence")
        print(f"{outputIndent}{pageSequenceOutput}")
        print(f"--------------------------------------------")
        lru.outputPageFrameHistory()
        print(f"{outputIndent}{lru.outputPageFaultHistory()}")
        print("\n")

    lru.countPageFaults()

    if lru.pageFaultScore == 0:
        print("No page faults")
    print(f"Page fault score is {lru.pageFaultScore}")

if __name__ == "__main__":
    memoryManagement()