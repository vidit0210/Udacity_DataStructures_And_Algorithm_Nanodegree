class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = 0


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        if(self.head is None):
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def remove_first(self):
        newHead = self.head.next
        self.head = newHead
        self.length -= 1

    def remove_last(self):
        current = self.head
        newtail = current
        while(current.next):
            newtail = current
            current = current.next
        self.tail = newtail
        self.tail.next = None
        self.length -= 1
        return current.value

    def getNode(self, index):
        count = 0
        head = self.head
        while(index != count):
            head = head.next
            count += 1
        return head

    def remove(self, index):
        if index == 0:
            return self.remove_first()
        if index == self.length-1:
            return self.remove_last()
        prevNode = self.getNode(index-1)
        removeNode = prevNode.next
        prevNode.next = removeNode.next
        self.length -= 1

    def print_chain(self):
        arr = []
        head = self.head
        while(head):
            arr.append(head.value)
            head = head.next

        return arr


ll = LinkedList()
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.remove(0)
print(ll.print_chain())


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.list = LinkedList()
        self.data = {}
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        val = self.data.get(key)
        if(val):
            return val
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.data.get(key):
            return
        if self.capacity == self.list.length:
            remove_key = self.list.remove_last()
            del self.data[remove_key]

        self.list.push(key)
        self.data[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(3))     # return -1

#Test Cases

our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)


print(our_cache.get(4))       # returns 4
print(our_cache.get(5))       # returns -1 Old Entry removed from the Data
print(our_cache.get(6))       # returns 6
