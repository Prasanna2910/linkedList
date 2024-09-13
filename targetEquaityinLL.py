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
    def finding(self,tar):
        i = self.head
        found = False
        store = []
        while i:
            j = self.head
            while j:
                if i.data+j.data == tar and i.data not in store and j.data not in store:
                    store.append(i.data)
                    store.append(j.data)
                    # return store
                    # print(i.data,j.data)
                    found = True
                    # break
                j = j.next
            i = i.next
        print(*store)
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
myList = LinkedList()
a,b = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(a-1,-1,-1):
    myList.insert(arr[i])

myList.finding(b)
    # print("True")