class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        for i in range(n):
            if s[i] == 'R':
                nums[i] += d
            else:
                nums[i] -= d
        nums.sort()
        print(nums)
        dis = [y - x for x, y in pairwise(nums)]
        print(dis)
        pre = 0
        for i in range(len(dis)):
            dis[i] = (i+1) * dis[i] + pre
            pre = dis[i]
        return sum(dis) % (10 ** 9 + 7)
        
