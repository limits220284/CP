class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        cnt = 0
        i = 0
        while cnt < 10000:
            cnt += 1
            num1 -= num2
            if num1 <= 0:
                return -1
            s = bin(num1)[2::]
            if s.count('1') <= cnt and cnt <= num1:
                return cnt
        return -1