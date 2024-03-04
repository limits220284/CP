class Solution:
    def digitCount(self, num: str) -> bool:
        dic=Counter([int(x) for x in num])
        for i,x in enumerate(num):
            if dic[i]!=int(x):
                return False
        return True