class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        pre = [0] * (n + 1)
        pre[0] = 1e9
        l = 0
        tot = 0
        ans = float('inf')
        for r, x in enumerate(arr):
            tot += arr[r]
            while tot > target:
                tot -= arr[l]
                l += 1
            if tot == target:
                print('ok')
                ans = min(ans, r - l + 1 + pre[l])
                pre[r + 1] = min(pre[r], r - l + 1)

            else:
                pre[r + 1] = pre[r]
        return ans if ans < 1e9 else -1
