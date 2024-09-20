class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
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
            newNode.prev = temp
    def insertAtK(self,tar,val,n):
        newnode = Node(val)
        if tar == 0:
            newnode.next = self.head
            if self.head:
                self.head.prev = newnode
            self.head = newnode
            return
        
        temp = self.head
        count = 0
        
        while temp:
            if count == tar-1:
                newnode.next = temp.next
                if temp.next:
                    temp.next.prev = newnode
                temp.next = newnode
                newnode.prev = temp
                return
            temp = temp.next
            count = count + 1
        # if tar>n:
        #     temp.next = newnode
        #     newnode.prev = temp
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
        print()
my = LinkedList()
n,tar,val = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(len(arr)):
    my.insert(arr[i])
my.insertAtK(tar,val,n)
my.display()
    


    
    