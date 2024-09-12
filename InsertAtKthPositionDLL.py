class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
    
    def insertAtIndex(self,data,k):
        newNode = Node(data)
        if self.head is None:
            return
        temp = self.head
        count = 0
        while temp:
            count = count + 1
            if count == k:
                newNode.next = temp.next
                temp.next = newNode
                newNode.prev = temp
                temp.next.prev = newNode
                temp = temp.next
                return temp
            temp = temp.next

mylist = LinkedList()
n,k,val = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(len(arr)-1,-1,-1):
    # print(i)
    mylist.insertAtBeginning(arr[i])
mylist.insertAtIndex(val,k)
mylist.display()