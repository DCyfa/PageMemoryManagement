
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, pageFrameCount):
        self.capacity = pageFrameCount
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.pageFrameHistory = [[" " for i in range(15)] for i in range(4)]
        self.pageFaultHistory = []

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insertAtHead(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def updatePage(self, key):

        if key in self.cache:
            node = self.cache[key]

            # removes node from list and replaces it at head - most recently used
            self.remove(node)
            self.insertAtHead(node)
            return node.value # returns page frame of page sequence num
        return -1 # does not exist in cache
    
    def insertNewPage(self, key, value):

        if key in self.cache:
            self.remove(self.cache[key])

        newNode = Node(key, value)
        self.insertAtHead(newNode)
        self.cache[key] = newNode

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


    
def inputPageOrder():

    pageSequence = []

    while len(pageSequence) != 15:

        pageNum = int(input("Enter a page number (0-9): "))
        pageSequence.append(pageNum)

    print("Full page sequence has been entered")
    print(pageSequence)

    return pageSequence

def memoryManagement():

    pageSequence = inputPageOrder()
    outputIndent = " " * len("Page Frame 0: ")
    pageSequenceOutput = " ".join(map(str, pageSequence))
    capacity = 4
    lru = LRUCache(capacity)

    for timeStep in range(len(pageSequence)):
        pageNumStr = str(pageSequence[timeStep])
        pageStr = "Page " + pageNumStr
        if lru.updatePage(pageNumStr) == -1:
            lru.insertNewPage(pageNumStr, pageStr)
            lru.pageFaultHistory.append("*")
        lru.updatePageFrameHistory(timeStep)
        print(f"{outputIndent}     The paging sequence")
        print(f"{outputIndent}{pageSequenceOutput}")
        lru.outputPageFrameHistory()
        print(f"{outputIndent}{lru.outputPageFaultHistory()}")
        print("\n")

if __name__ == "__main__":
    memoryManagement()