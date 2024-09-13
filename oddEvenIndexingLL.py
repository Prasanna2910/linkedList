class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def oddEvenList(self):
        if not self.head or not self.head.next:
            return
        odd = self.head
        even = self.head.next
        store = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = store
            
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
myList = LinkedList()
a = int(input())
arr = list(map(int,input().split()))
for i in range(a-1,-1,-1):
    myList.insert(arr[i])
myList.oddEvenList()
myList.display()