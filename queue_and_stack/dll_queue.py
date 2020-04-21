import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.node = ListNode(None)
        self.dll = DoublyLinkedList(self.node)

    def enqueue(self, value):
        if self.dll.head.value is None:
            self.dll.head.value = value
        else:
            self.dll.add_to_tail(value)

    def dequeue(self):
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


test_q = Queue()
print(test_q.len())
test_q.enqueue(3)
test_q.enqueue(5)
test_q.enqueue(7)
test_q.dequeue()
test_q.dequeue()
test_q.dequeue()
print(test_q.dequeue())
