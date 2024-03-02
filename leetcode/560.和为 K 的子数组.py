class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 两数之和
        pre = [0]
        for x in nums: pre.append(pre[-1] + x)
        cnt = Counter()
        ans = 0
        for i, x in enumerate(pre):
            if x - k in cnt:
                ans += cnt[x-k]
            cnt[x] += 1
        return ans
            