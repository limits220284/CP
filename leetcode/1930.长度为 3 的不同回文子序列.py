class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        res = 0
        # 前缀/后缀字符状态数组
        pre = [0] * n
        suf = [0] * n
        for i in range(n):
            # 前缀 s[0..i-1] 包含的字符种类
            pre[i] = (pre[i-1] if i else 0) | (1 << (ord(s[i]) - ord('a')))
        for i in range(n - 1, -1, -1):
            # 后缀 s[i+1..n-1] 包含的字符种类
            suf[i] = (suf[i+1] if i != n - 1 else 0) | (1 << (ord(s[i]) - ord('a')))
        # 每种中间字符的回文子序列状态数组
        ans = [0] * 26
        for i in range(1, n - 1):
            ans[ord(s[i])-ord('a')] |= pre[i-1] & suf[i+1]#记录当前该元素前缀和后缀的共同元素，如果有两个相同的元素，就代表当前该元素可以组成两个子序列
        # 更新答案
        for i in range(26):
            res += bin(ans[i]).count("1")
        return res