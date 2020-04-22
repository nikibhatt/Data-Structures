from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage_dict = {}
        self.dll = DoublyLinkedList()
        self.size = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage_dict:
            self.dll.move_to_front(self.storage_dict[key])
            return(self.storage_dict[key].value)
        else:
            return None



    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage_dict:
            self.storage_dict[key].value = value
            existing_node = self.storage_dict[key]
            self.dll.move_to_front(existing_node)
            return
        if self.size == self.limit:
            oldest_node = self.dll.tail
            self.dll.delete(oldest_node)
            del self.storage_dict[oldest_node]
            new_node = ListNode(value)
            self.storage_dict.update({key:new_node})
            self.dll.move_to_front(new_node)
        else:
            new_node = ListNode(value)
            self.storage_dict.update({key:new_node})
            self.dll.add_to_head(new_node)
            self.size += 1


# cache = LRUCache(3)
# cache.set('item1', 'a')
# cache.set('item2', 'b')
# cache.set('item3', 'c')
# print(cache.get('item1'))
# print(cache.get('item2'))
# print(cache.get('item3'))
# print(cache.size)
# cache.set('item4', 'd')
# print(cache.size)
# print(cache.get('item1'))
# print(cache.get('item3'))
# print(cache.get('item4'))
# print(cache.get('item2'))
