class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        # a, b长度不一样
        # 如果要满足第三个条件，需要计算出现最多次数的字母即可
        m, n = len(a), len(b)
        dic = Counter(a + b)
        ans3 = m + n - max(dic.values())
        # 如果要满足第二个条件呢？
        def work(a, b):
            cnta = [0] * 26
            cntb = [0] * 26
            mxa = 'a'
            mxb = 'a'
            for c in a:
                inx = ord(c) - ord('a')
                cnta[inx] += 1
                mxa = max(mxa, c)
            for c in b:
                inx = ord(c) - ord('a')
                cntb[inx] += 1
                mxb = max(mxb, c)
            # print(cnta, cntb)
            # 枚举a的最大值, 和b的最小值
            ans = inf
            for i in range(26):
                for j in range(i+1, 26):
                    ta, tb = 0, 0
                    for k in range(26):
                        if k > i:
                            ta += cnta[k]
                    for k in range(26):
                        if k < j:
                            tb += cntb[k]
                    ans = min(ans, ta + tb)
            return ans
        ans1 = work(a, b)
        ans2 = work(b, a)
        return min(ans1, ans2, ans3)
            