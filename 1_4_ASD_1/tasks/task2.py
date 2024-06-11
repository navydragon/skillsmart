class Node:

    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        arr = [];
        node = self.head
        while node != None:
            if node.value == val:
                arr.append(node)
            node = node.next
        if len(arr) > 0:
            return arr
        return arr
        
    def delete(self, val, all=False):
        node = self.head
        count = 0
        while node is not None:
            prev_node = node.prev
            next_node = node.next
            if node.value == val:
                if node == self.head and node == self.tail:
                    self.head = None
                    self.tail = None
                    return
                elif node == self.head:
                    self.head = node.next
                    next_node.prev = None
                elif node == self.tail:
                    self.tail = node.prev
                    prev_node.next = None
                else:
                    prev_node.next = next_node
                    next_node.prev = prev_node
                count += 1
                next_node = node.next
                node.prev = None
                node.next = None
                if (all == False):
                    return count
            node = next_node
        return count 
        
    def clean(self):
        node = self.head
        self.head = None
        self.tail = None
        while node is not None:
            next_node = node.next
            node.next = None
            node.prev = None
            node = next_node

    def len(self):
        count = 0
        node = self.head
        while node != None:
            count = count + 1
            node = node.next
        return count
        
    def insert(self, afterNode, newNode):
        if afterNode == None:
            self.add_in_tail(newNode)
            return True
        next_node = afterNode.next
        newNode.next = afterNode.next
        newNode.prev = afterNode
        afterNode.next = newNode
        if (next_node != None):
            next_node.prev = newNode
        if afterNode == self.tail:
            self.tail = newNode
        pass
    
    def add_in_head(self, newNode):
        if self.tail is None:
            self.tail = newNode
            newNode.next = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
        newNode.prev = None
        pass