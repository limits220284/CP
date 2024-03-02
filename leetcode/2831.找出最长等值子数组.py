class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic = defaultdict(list)
        for i, x in enumerate(nums):
            dic[x].append(i)
        ans = 1
        for i, arr in dic.items():
            m = len(arr)
            left, tot = 0, k
            for j in range(1, m):
                while tot < arr[j] - arr[j-1] - 1:
                    left += 1
                    tot += arr[left] - arr[left-1] - 1
                tot -= arr[j] - arr[j-1] - 1
                ans = max(ans, j - left + 1)
        return ans
        