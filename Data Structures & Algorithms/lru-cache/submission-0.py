class Node:
    def __init__(self,key:int=0,value:int=0):
        self.key=key
        self.value=value
        self.nxt=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_d={}
        self.capacity=capacity

        self.right,self.left=Node(),Node()
        self.left.nxt=self.right
        self.right.prev=self.left
    
    def remove(self,node):
        node.prev.nxt=node.nxt
        node.nxt.prev=node.prev

    def insert(self,node):
        node.nxt=self.right
        node.prev=self.right.prev
        self.right.prev.nxt=node
        self.right.prev=node
        

    def get(self, key: int) -> int:
        if key in self.cache_d:
            self.remove(self.cache_d[key])
            self.insert(self.cache_d[key])
            return self.cache_d[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_d:
            self.remove(self.cache_d[key])
        self.cache_d[key] = Node(key,value)
        self.insert(self.cache_d[key])

        if len(self.cache_d)>self.capacity:
            lru=self.left.nxt
            self.remove(lru)
            del self.cache_d[lru.key]

        
