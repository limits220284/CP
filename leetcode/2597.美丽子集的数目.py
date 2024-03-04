class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = -1  # 去掉空集
        cnt = Counter()  # 用数组实现比哈希表更快
        def dfs(i: int) -> None:  # 从 i 开始选
            nonlocal ans
            ans += 1
            if i == len(nums):
                return
            for j in range(i, len(nums)):  # 枚举选哪个
                x = nums[j]
                if cnt[x - k] == 0 and cnt[x + k] == 0:
                    cnt[x] += 1  # 选
                    dfs(j + 1)
                    cnt[x] -= 1  # 恢复现场
        dfs(0)
        return ans