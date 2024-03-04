class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        s = bin(n)[2:]
        a,b=0,0
        for i,x in enumerate(s[::-1]):
            if x == '1':
                if i%2 == 1:
                    b+=1
                else:
                    a+=1
        return [a,b]
        