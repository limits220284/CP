class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mask=0
        for i in allowed:
            mask|=1<<ord(i)-ord('a')
        cnt=0
        for word in words:
            mask1=0
            for i in word:
                mask1|=1<<ord(i)-ord('a')
            cnt+=(mask|mask1)==mask
        return cnt