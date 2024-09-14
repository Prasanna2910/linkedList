class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        self.head = prev
        # return self.head

    def insert(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

# Create a linked list object
mylist = LinkedList()

# Get input from the user
a = int(input())
arr = list(map(int, input().split()))

# Insert elements into the linked list in reverse order
for i in range(len(arr)-1,-1,-1):
    mylist.insert(arr[i])

# Reverse the linked list
mylist.reverse()

# Display the linked list
mylist.display()