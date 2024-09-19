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
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
    def middle(self):
        if not self.head or not self.head.next:
            return self.head
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
        print()
my = LinkedList()
a = int(input())
arr = list(map(int,input().split()))
for i in range(len(arr)):
    my.insert(arr[i])
middleele = my.middle()
if middleele:
    print(middleele.data)
else:
    print("list is empty")