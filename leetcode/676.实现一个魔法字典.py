class MagicDictionary:

    def __init__(self):
        self.dic={}

    def buildDict(self, dictionary: List[str]) -> None:
        for i in range(len(dictionary)):
            self.dic[dictionary[i]]=True

    def search(self, searchWord: str) -> bool:
        n=len(searchWord)
        for i in range(n):
            x=list(searchWord)
            for j in range(1,26):
                x[i]=chr((ord(searchWord[i])-ord('a')+j)%26+ord('a'))
                if self.dic.get(''.join(x)):
                    return True
        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)