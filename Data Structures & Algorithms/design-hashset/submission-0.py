class MyHashSet:

    def __init__(self):
        self.key = set()

    def add(self, key: int) -> None:
        self.key.add(key)

    def remove(self, key: int) -> None:
        self.key.discard(key)

    def contains(self, key: int) -> bool:
        return True if key in self.key else False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)