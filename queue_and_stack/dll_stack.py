import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.node = ListNode(None)
        self.dll = DoublyLinkedList(self.node)

    def push(self, value):
        if self.dll.head.value is None:
            self.dll.head.value = value
        else:
            self.dll.add_to_head(value)

    def pop(self):
        if self.dll:
            return(self.dll.remove_from_head())
        else:
            return None

    def len(self):
        if self.dll:
            if self.dll.head.value is None:
                return 0
            else:
                return(self.dll.length)
        else:
            return 0
