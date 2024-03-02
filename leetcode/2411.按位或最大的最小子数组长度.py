class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ors = []
        for i in range(n - 1, -1, -1):
            num = nums[i]
            ors.append([0, i])
            for p in ors:
                p[0] |= num # 都或上num
            k = 0
            for p in ors:
                if p[0] != ors[k][0]:
                    k += 1
                    ors[k] = p
                else:
                    ors[k][1] = p[1]
            del ors[k + 1:]
            ans[i] = ors[0][1] - i + 1
        return ans