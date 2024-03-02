@cache
def work(x):
    cnt = Counter()
    i = 2
    while i <= x // i:
        if x % i == 0:
            b = 0
            while x % i == 0:
                x //= i
                b += 1
            cnt[i] += b
        i += 1
    if x > 1:
        cnt[x] += 1
    return cnt
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        factors = [defaultdict(int) for _ in range(n)]
        for k, x in enumerate(nums):
            factors[k] = work(x)
        suf = defaultdict(int)
        for i, factor in enumerate(factors):
            for k, v in factor.items():
                suf[k] += v
        pre = Counter()
        for i in range(n - 1):
            x_factor = factors[i]
            flag = True
            for k, v in x_factor.items():
                pre[k] += v
                suf[k] -= v
            for k, v in pre.items():
                if suf[k] != 0:
                    flag = False
                    break
            if flag:
                return i
        return -1