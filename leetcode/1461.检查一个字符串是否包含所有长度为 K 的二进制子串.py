class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < (1 << k) + k - 1:
            return False
        
        num = int(s[:k], base=2)
        exists = set([num])

        for i in range(1, len(s) - k + 1):
            num = (num - ((ord(s[i - 1]) - 48) << (k - 1))) * 2 + (ord(s[i + k - 1]) - 48)
            exists.add(num)
        
        return len(exists) == (1 << k)