class Node(object):
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.len = 0
        self.cache = {}

    def length(self):
        return self.len

    def full(self):
        return self.len == self.capacity

    def append(self, key, val):
        node = Node(key, val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

        self.cache[key] = node
        self.len += 1

    def set(self, key, value):
        if key in self.cache:
            old_val = self.cache[key].val
            self.remove(key)
            self.append(key, value)
        else:
            if self.full():
                self.remove(self.head.key)
            self.append(key, value)

    def get(self, key):
        try:
            val = self.cache[key].val
        except KeyError:
            return -1
        self.remove(key)
        self.append(key, val)
        return val

    def remove(self, key):
        node = self.cache[key]
        if node.prev is not None and node.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.prev is not None and not node.next:
            # tail
            self.tail = node.prev
            node.prev.next = None
        elif node.next is not None and not node.prev:
            # head
            self.head = node.next
            node.next.prev = None
        else:
            self.head = self.tail = None

        self.cache.pop(key)
        self.len -= 1

def main():
    lru = LRUCache(5)
    lru.set(1,'one')
    lru.set(2, 'two')
    lru.set(2, 'three')
    lru.set(4, 'four')
    lru.set(1,'five')
    lru.set(3, 'six')

main()