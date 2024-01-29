class Node:

    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

        # Left -> LRU
        # Right -> Most recently used

    # Remove a node from it's position in DLL
    def remove(self, node):

        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    # Insert a node to the Most recently used side (Right side)
    def insert(self, node):

        prevNode = self.right.prev
        nextNode = self.right

        prevNode.next = node
        nextNode.prev = node

        node.prev = prevNode
        node.next = nextNode
        

    def get(self, key: int) -> int:

        if(key in self.d):

            # Update to Most recently used
            self.remove(self.d[key])
            self.insert(self.d[key])

            return self.d[key].val
        
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        if(key in self.d):
            self.remove(self.d[key])

        newNode = Node(key, value)
        self.d[key] = newNode
        self.insert(self.d[key])

        if(len(self.d)>self.cap):
            
            # Remove node from LRU
            nodeToBeRemoved = self.left.next
            del self.d[nodeToBeRemoved.key]
            self.remove(nodeToBeRemoved)





        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)