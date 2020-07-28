from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return - 1
        # move_to_end(key, last=True) moved to the right, if last is true (default) or to the start if last is false.
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)  # last = False is for FIFO , last = True is for LIFO


cache = LRUCache(5)

cache.put(1, 'a')
cache.put(2, 'b')
cache.put(3, 'c')
cache.put(4, 'd')
cache.put(5, 'e')
print(cache)
cache.get(1)
print(cache)
cache.get(3)
print(cache)
cache.get(4)
print(cache)
cache.put(6, 'f')
print(cache)
print(cache.get(2))
print(cache)


