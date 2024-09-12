class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    def sorting(self):
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp and temp.next:
                if temp.data >temp.next.data:
                    store = temp.next.data
                    temp.next.data = temp.data
                    temp.data = store
                    swapped = True
                temp = temp.next
        return self.head
myList = LinkedList()
a = list(map(int,input().split()))
for i in range(len(a)-1,-1,-1):
    myList.insert(a[i])
myList.sorting()
myList.display()
    
                
