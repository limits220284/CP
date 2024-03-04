class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = Counter(nums[:k - 1])
        s = sum(nums[:k - 1])
        for in_, out in zip(nums[k - 1:], nums):
            cnt[in_] += 1  # 移入元素
            s += in_
            if len(cnt) == k:
                ans = max(ans, s)
            cnt[out] -= 1  # 移出元素
            if cnt[out] == 0:
                del cnt[out]  # 重要：及时移除个数为 0 的数据
            s -= out
        return ans