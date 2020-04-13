class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        arr = []
        if self.head == None:
            return
        else:
            arr.append(self.head)
            if self.head.next != None:
                self.printListHelper(arr, self.head.next)
            else:
                return self.head.value

    def printListHelper(self, arr, nextNode):
        if nextNode != None:
            arr.append(nextNode)
            self.printListHelper(arr, nextNode.next)
        for i in arr:
            print(i.value)
        return 



    def setHead(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)
        

    def setTail(self, node):
        if self.tail == None:
	        self.head = node
	        self.tail = node
        else:
	        self.insertAfter(self.tail, node)
        

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
	        return
        if node.prev == None:
            self.head = nodeToInsert
            nodeToInsert.prev = None
            nodeToInsert.next = node
            node.prev = nodeToInsert
            
        else:
            nodeToInsert.prev = node.prev
            node.prev.next = nodeToInsert
            node.prev = nodeToInsert
            nodeToInsert.next = node
        

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        if node.next == None:
            self.tail = nodeToInsert
            nodeToInsert.next = None
            node.next = nodeToInsert
            nodeToInsert.prev = node
        else:
            nodeToInsert.next = node.next
            node.next.prev = nodeToInsert
            node.next = nodeToInsert
            nodeToInsert.prev = node

    def insertAtPosition(self, position, nodeToInsert):
        currentNode = self.head
        pos = 1
        while position != pos:
            currentNode = currentNode.next
            pos += 1
            if currentNode == None:
                return
        self.insertBefore(currentNode, nodeToInsert)

    def removeNodesWithValue(self, value):
        currentNode = self.head
        atEnd = 1
        while atEnd != None:
            atEnd = currentNode.next
            if currentNode.value == value:
                self.remove(currentNode)
            currentNode = currentNode.next


    def remove(self, node):
        currentNode = self.head
        while currentNode != node:
            currentNode = currentNode.next
        if currentNode == self.head:
            currentNode.next.prev = None
            self.head = currentNode.next
        elif currentNode == self.tail:
            currentNode.prev.next = None
            self.tail = currentNode.prev
        else:
            currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev


    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(4)
someList = DoublyLinkedList()
someList.setTail(node1)
someList.setHead(node2)
someList.setTail(node5)
someList.insertAfter(node1, node3)
someList.insertAtPosition(2, node4)
#someList.remove(node4)
someList.removeNodesWithValue(4)


