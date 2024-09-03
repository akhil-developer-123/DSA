class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    
    def printNode(self, a, b, c):
        print("node value", self.data)
    

class SinglyLinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    
    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end=' -> ')
            currentNode = currentNode.next
        print()
    
    def insertAtBeginning(self, value):
        newNode = Node(value)
        if self.head is None:
            # list is empty, the new node itself is head and tail
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def insertAtEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            last_node = self.tail
            last_node.next = newNode
            self.tail = newNode
    
    def insertAtMiddle(self, insertAfter, value):
        if self.head is None:
            print("linkedlist is empty, cannot find ", insertAfter)
            return
        if self.tail.data == insertAfter:
            self.insertAtEnd(value)
            return
        currentNode = self.head
        while currentNode and currentNode.data != insertAfter:
            currentNode = currentNode.next
        # fails when currentNode = None
        # fails when currentNode.data == insertAfter
        newNode = Node(value)
        if currentNode is not None and currentNode.data == insertAfter:
            tmp = currentNode.next
            currentNode.next = newNode
            newNode.next = tmp
        else:
            print("cannot find ", insertAfter)
    
    def deleteHead(self):
        if self.head is None:
            print("empty linkedlist, cannot delete")
        else:
            first_node = self.head
            second_node = self.head.next
            first_node.next = None
            self.head = second_node
    
    def deleteTail(self):
        if self.tail is None:
            print("empty linkedlist, cannot delete")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            currentNode = self.head
            while currentNode and currentNode.next != self.tail:
                currentNode = currentNode.next
            if currentNode is not None:
                currentNode.next = None
            self.tail = currentNode
    
    def deleteMiddle(self, value):
        # delete the first occurence of value from the list
        if self.head is None:
            print("no values in the linkedlist")
            return
        
        if self.head.data == value:
            self.deleteHead()
            return
        
        first, second = self.head, self.head.next
        while first and second and second.data != value:
            first = first.next
            second = second.next
        if first and second:
            if second == self.tail:
                self.deleteTail()
                return
            third = second.next
            first.next = third
            second.next = None # cleanup
            

    
node1 = Node(100)
node2 = Node(200)
node3 = Node(300)

# 100 -> 200 -> 300
# link the nodes
node1.next = node2
node2.next = node3





# create a linkedList
head, tail = node1, node3
linkedList = SinglyLinkedList(head, tail)
linkedList.printList()
# linkedList.deleteHead()
# linkedList.printList()

print(linkedList.head.data)
print(linkedList.tail.data)


# linkedList.deleteTail()
linkedList.deleteMiddle(300)
linkedList.printList()

print(linkedList.head.data)
print(linkedList.tail.data)



# operations on LinkedList
# linkedList.insertAtBeginning(400)
# linkedList.printList()

# linkedList.insertAtEnd(500)
# linkedList.printList()

# linkedList.insertAtMiddle(200, 600)
# linkedList.printList()

# linkedList.insertAtMiddle(1000, 700)
# linkedList.insertAtMiddle(2000, 700)
