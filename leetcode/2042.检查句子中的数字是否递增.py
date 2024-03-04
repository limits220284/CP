class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        pre=-1
        cnt=0
        s+=' '
        for i,c in enumerate(s):
            if c==' ' and s[i-1].isdigit():
                if cnt<=pre:
                    return False
                pre=cnt
                cnt=0
            elif c.isdigit():
                cnt=cnt*10+int(c)
        return True