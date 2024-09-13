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
    def cycleCheck(self):
        if not self.head:
            return False
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
myList = LinkedList()
a = int(input())
arr = list(map(int,input().split()))
target = int(input())
for i in range(len(arr)-1,-1,-1):
    myList.insert(arr[i])
if myList.cycleCheck():
    print("True")
else:
    print("False")
    
                