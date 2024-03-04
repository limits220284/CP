class Skiplist:

    def __init__(self):
        self.dic=defaultdict(int)

    def search(self, target: int) -> bool:
        if self.dic[target]:
            return True
        return False

    def add(self, num: int) -> None:
        self.dic[num]+=1

    def erase(self, num: int) -> bool:
        if not self.dic[num]:
            return False
        self.dic[num]-=1
        return True
            



# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)