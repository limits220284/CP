class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def f(s):
            # 求多少子串恰好出现k次
            # 枚举字串有多少个字母m
            # 长度恰好为m * k的窗口内，是否满足每个字母恰好出现k次
            nn = len(s)
            res = 0
            for m in range(1, 27):
                size = m * k
                if size > len(s):
                    break
                cnt = Counter()
                for i in range(nn):
                    if i < size - 1:
                        cnt[s[i]] += 1
                        continue
                    cnt[s[i]] += 1
                    if all(v == 0 or v == k for v in cnt.values()):
                        res += 1
                    cnt[s[i - size + 1]] -= 1
            return res
        n = len(word)
        i = 0
        ans = 0
        while i < n:
            start = i
            i += 1
            while i < n and abs(ord(word[i]) - ord(word[i - 1])) <= 2:
                i += 1
            ans += f(word[start: i])
        return ans