# https://leetcode.com/problems/lru-cache/

class LRUCache:
    class ListNode:
        def __init__(self, key, val, prev=None, next=None) -> None:
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.cacheHead = None
        self.cacheTail = None
        self.capacity = capacity
        self.noOfItems = 0
        self.keys = {}

    def get(self, key: int) -> int:
        value = -1
        if key in self.keys:
            node = self.keys[key]
            value = node.val
            if node.next:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.cacheHead = self.cacheHead.next
                node.next.prev = node.prev
                self.cacheTail.next = node
                node.prev = self.cacheTail
                node.next = None
                self.cacheTail = self.cacheTail.next
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key].val = value
            node = self.keys[key]
            if node.next:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.cacheHead = self.cacheHead.next
                node.next.prev = node.prev
                self.cacheTail.next = node
                node.prev = self.cacheTail
                node.next = None
                self.cacheTail = self.cacheTail.next
            return

        if self.noOfItems == 0:
            self.cacheHead = self.ListNode(key, value)
            self.cacheTail = self.cacheHead
            self.keys[key] = self.cacheHead
            self.noOfItems = self.noOfItems + 1
            return

        if self.noOfItems == self.capacity:
            del self.keys[self.cacheHead.key]
            self.cacheHead = self.cacheHead.next
            if not self.cacheHead:
                self.noOfItems = 0
                self.cacheTail = None
                self.put(key, value)
                return
            else:
                self.cacheHead.prev = None
        else:
            self.noOfItems = self.noOfItems + 1
        node = self.ListNode(key, value, self.cacheTail, None)
        self.keys[key] = node
        self.cacheTail.next = node
        self.cacheTail = self.cacheTail.next

    def display(self):
        print('-'*30)
        node = self.cacheHead
        while node:
            print(node.val, end=' ')
            node = node.next

        print()

        node = self.cacheTail
        while node:
            print(node.val, end=' ')
            node = node.prev
        print()
        print('-'*30)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


cache = LRUCache(5)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.put(4, 4)
cache.put(5, 5)
cache.display()
print('Get', cache.get(1))
cache.display()
print('Put', 6)
cache.put(6, 6)
cache.display()
print('Get', cache.get(5))
cache.display()
print('Put', 7)
cache.put(7, 7)
cache.display()


print('*'*30)
cache = LRUCache(1)
cache.put(2, 1)
print(cache.get(2))
cache.display()


print('*'*30)
cache = LRUCache(1)
cache.put(2, 1)
print(cache.get(2))
cache.display()
cache.put(3, 2)
print(cache.get(2))
print(cache.get(3))


print('*'*30)
cache = LRUCache(2)
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
cache.display()
print(cache.get(1))
print(cache.get(2))
cache.display()
