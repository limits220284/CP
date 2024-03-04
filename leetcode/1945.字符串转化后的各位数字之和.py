class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numb=''
        for x in s:
            numb+=str(ord(x)-ord('a')+1)
        while k:
            numb=str(sum([int(x) for x in numb]))
            k-=1
        return int(numb)