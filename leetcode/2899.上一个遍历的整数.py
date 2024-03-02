class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        n = len(words)
        k = 0
        pre = None
        cnt = 0
        ans = []
        num = []
        for i, x in enumerate(words):
            if x == 'prev':
                k += 1
                if k > cnt:
                    ans.append(-1)
                else:
                    ans.append(num[::-1][k-1])
            else:
                cnt += 1
                k = 0
                num.append(int(x))
        return ans