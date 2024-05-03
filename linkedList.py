class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def prepend(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def append(self,data):
        newNode  = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while self.head:
            temp = temp.next
        temp.next = newNode
    def popFront(self):
        if self.head is None:
            return "Empty"
        self.head = self.head.next
    def popEnd(self):
        if self.head is None:
            return
        if self.head.next is None:
            return self.head = None
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
    def FindtheElement(self,value):
        temp = self.head
        store = 0
        while temp.next:
            if temp.data == value:
                return store
            store = store+1
            temp = temp.next
        return "Element nont found"
            
            
        
        
    
        

        
        
        
    