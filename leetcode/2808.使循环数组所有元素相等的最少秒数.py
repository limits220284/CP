class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        n = len(nums)
        for i in range(n):
            dic[nums[i]].append(i)
        
        mx = len(nums)
        for k, v in dic.items():
            c = (dic[k][0] - 0)+(n - 1 - dic[k][-1])
            for i in range(1,len(dic[k])):
                c = max(c,dic[k][i] - dic[k][i-1] - 1)
            mx = min(mx,c)
        return (1 + mx) // 2