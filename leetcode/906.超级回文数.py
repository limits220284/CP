class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        UP = 10 ** (len(str(int(sqrt(int(right))))) // 2 + 1)
        ans = 0
        def check(ss):
            return ss == ss[::-1]
        for i in range(1, UP):
            # 枚举奇数
            s = str(i)
            ss = s + s[::-1][1:]
            ss = int(ss)
            if check(str(ss * ss)):
                if int(left) <= ss ** 2 <= int(right):
                    ans += 1
            # 枚举偶数
            s = str(i)
            ss = s + s[::-1]
            ss = int(ss)
            if check(str(ss * ss)):
                if int(left) <= ss ** 2 <= int(right):
                    ans += 1
        return ans
