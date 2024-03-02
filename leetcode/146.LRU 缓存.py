class Node:
    def __init__(self, key = 0, value = 0, pre = None, next = None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.pre = self.dummy
        self.dummy.next = self.dummy
        self.keynode = defaultdict(int)
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
    def add(self, x):
        x.pre = self.dummy
        x.next = self.dummy.next
        x.pre.next = x
        x.next.pre = x
    def get(self, key: int) -> int:
        if key in self.keynode:
            self.remove(self.keynode[key])
            self.add(self.keynode[key])
            return self.keynode[key].value
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.keynode:
            self.remove(self.keynode[key])
            self.add(self.keynode[key])
            self.keynode[key].value = value
        else:
            self.keynode[key] = Node(key, value)
            self.add(self.keynode[key])
            if len(self.keynode) > self.capacity:
                # 删除尾部元素
                backnode = self.dummy.pre
                self.remove(backnode)
                del self.keynode[backnode.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)