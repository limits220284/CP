class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        arr=[0]
        for x in nums:
            arr.append(x+arr[-1])
        cnt=0
        dic=defaultdict(int)
        for x in arr:
            if x%k in dic:
                cnt+=dic[x%k]
            dic[x%k]+=1
        return cnt