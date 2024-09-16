lass Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
    
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    def palindrome(self):
        if not self.head or not self.head.next:
            return True
        
        # Find the middle of the list
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list
        second_half = self.reverse(slow.next)
        slow.next = None  # Cut off the first half
        
        # Compare the two halves
        first_half = self.head
        while first_half and second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Test the implementation
mylist = LinkedList()
arr = [1, 2, 4, 5, 1]
for i in range(len(arr)):
    mylist.insert(arr[i])

print("Original list:")
mylist.display()

if mylist.palindrome():
    print("The linked list is a palindrome")
else:
    print("The linked list is not a palindrome")