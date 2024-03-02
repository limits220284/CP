#
# @lc app=leetcode.cn id=1032 lang=python3
#
# [1032] 字符流
#

# @lc code=start
class StreamChecker:
    def insert(self, s) -> None:
        Node = self.Trie
        for x in s:
            Node = Node.setdefault(x, {})
        Node['cnt'] = True
    
    def find(self, s) -> bool:
        Node = self.Trie
        for x in s:
            if x not in Node:
                return False
            Node = Node[x]
            if 'cnt' in Node:
                return True
        return False

    def __init__(self, words: List[str]):
        self.ss = []
        self.Trie = {}
        for word in words:
            self.insert(word[::-1])
        
    def query(self, letter: str) -> bool:
        self.ss.append(letter)
        return self.find(reversed(self.ss))

