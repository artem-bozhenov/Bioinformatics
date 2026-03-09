class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self.head is None

    def enqueque(self, value):
        new_node = ListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
