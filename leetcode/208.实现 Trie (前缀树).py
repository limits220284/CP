class Trie:
    def __init__(self):
        self.Trie={}

    def insert(self, word: str) -> None:
        p=self.Trie
        for x in word:
            p=p.setdefault(x,{})#如果p[x]存在，则返回value值，否者设置value值为{}
        p['cnt']=p.get('cnt',0)+1

    def search(self, word: str) -> bool:
        p=self.Trie
        for x in word:
            if x not in p:
                return False
            p=p[x]
        if p.get('cnt') is None:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        p=self.Trie
        for x in prefix:
            if x not in p:
                return False
            p=p[x]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)