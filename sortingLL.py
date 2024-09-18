class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data: 
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result

    def getMiddle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortList(self):
        if not self.head or not self.head.next:
            return self.head

        middle = self.getMiddle(self.head)
        nextMiddle = middle.next
        middle.next = None

        leftHalf = LinkedList()
        rightHalf = LinkedList()
        leftHalf.head = self.sortListHelper(self.head)
        rightHalf.head = self.sortListHelper(nextMiddle)

        sortedList = self.merge(leftHalf.head, rightHalf.head)
        return sortedList
    
    def sortListHelper(self, head):
        if not head or not head.next:
            return head
        
        middle = self.getMiddle(head)
        nextMiddle = middle.next
        middle.next = None
        
        leftSorted = self.sortListHelper(head)
        rightSorted = self.sortListHelper(nextMiddle)
        
        return self.merge(leftSorted, rightSorted)

myList = LinkedList()
a = list(map(int, input().split()))
for i in range(len(a)):
    myList.insert(a[i])

myList.head = myList.sortList() 
myList.display()