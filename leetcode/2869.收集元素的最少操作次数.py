class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(range(1, k + 1))
        k = 0
        while nums:
            x = nums.pop()
            if x in cnt:
                del cnt[x]
            k += 1
            if len(cnt) == 0:
                return k
        return 0