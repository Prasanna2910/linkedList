class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            curr.prev = temp
            prev = curr
            curr = temp
        self.head = prev

    def insert(self, data):
        newNode = Node(data)
 
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

mylist = DoublyLinkedList()
a = int(input())
arr = list(map(int, input().split()))
for i in range(len(arr)-1, -1, -1):
    mylist.insert(arr[i])
mylist.reverse()
mylist.display()
