class Solution:
    def numDecodings(self, s: str) -> int:
        # 非常典型的线性dp
        # f[i] 表示以s[i]结尾的解码的方案数
        # f[i] = f[i]
        def check(ss):
            if len(ss) == 1 and ss != '0': return True
            if len(ss) == 2 and ss[0] != '0' and 1 <= int(ss) <= 26: return True
            return False
        n = len(s)
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(1, n+1):
            # 判断前面的一个是否合法
            # 判断前面的两个是否合法
            if i - 1 >= 0 and check(s[i-1]):
                f[i] += f[i-1]
            if i - 2 >= 0 and check(s[i-2] + s[i-1]):
                f[i] += f[i-2]
        # print(f)
        return f[-1]