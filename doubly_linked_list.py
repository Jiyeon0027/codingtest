# 한쪽으로만 링크를 연결하지 않고 양쪽으로! 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        
        self.head = Node(None)
        self.tail = None
        
        
    def __repr__(self):
        if self.nodeCount == 0:
            return 'DoublyLinkedList: empty'
        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s
    
    