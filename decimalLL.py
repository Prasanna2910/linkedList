class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        newNode = Node(data)
 
        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    def checking(self):
        # if self.head is None:
            
        stack = ""
        temp = self.head
        while temp:
            # print(temp.data)
            stack = stack + str(temp.data)
            
            temp = temp.next
        return stack
    
l1 = DoublyLinkedList()
l2 = DoublyLinkedList()
final =  DoublyLinkedList()
a = int(input())
store = 0
arr1 = list(map(int,input().split()))
b = int(input())
arr2 = list(map(int,input().split()))
for i in range(len(arr1)):
    l1.insert(arr1[i])

q = l1.checking()
store = store + int(q) 
for i in range(len(arr2)):
    l2.insert(arr2[i])
l2.checking()
store = store + int(l2.checking())
# print(store)
st = str(store)
for i in st:
    final.insert(i)
final.display()