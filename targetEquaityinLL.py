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
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
    def finding(self,tar):
        
        i = self.head
        store = []
        found = False
        while i:
            j = self.head
            while j:
                if i!=j and i.data+j.data == tar and i.data not in store and j.data not in store:
                    store.append(i.data)
                    store.append(j.data)    
                    found = True
                j = j.next
            i = i.next
        print(*store)
        if not store:
            print(-1)
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
        print()
myList = LinkedList()
a,b = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(len(arr)):
    myList.insert(arr[i])
myList.finding(b)
# myList.display()
        