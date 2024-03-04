class Solution:
    def specialArray(self, nums: List[int]) -> int:
        dic=Counter(nums)
        ans=list(dic.items())
        ans.sort(key=lambda x:x[0])
        s=sum(x[1] for x in ans)
        for x in range(len(nums)+1):
            if x in dic:
                if s==x:
                    return x
                s-=dic[x]
            else:
                if s==x:
                    return x
        return -1
                    