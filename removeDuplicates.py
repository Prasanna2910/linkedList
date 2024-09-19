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
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
        print()
    def checking(self):
        temp = self.head
        while temp:
            prev = temp
            check = temp.next
            while check:
                if check.data == temp.data:
                    prev.next = check.next
                    
                else:
                    prev = check
                check = check.next
            temp = temp.next 
my = LinkedList()
a = int(input())
arr = list(map(int,input().split()))
for i in range(len(arr)):
    my.insert(arr[i])
my.checking()
my.display()