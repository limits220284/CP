class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        # 对于这种题,可以通过排除法来进行思考,通过题目的数据量可以知道改题目复杂度不会很高
        # 所以最多O(n)解法,一次遍历
        # 对于这种删除的题目,删除的数如果不确定的话,就会考虑使用hash或者动态规划
        # 肯定算法本身和数字是谁并无太大关系
        n=len(nums)
        cnt=defaultdict(int)#x出现了几次
        num=defaultdict(int)#出现x次的数字有几个
        res=0
        mx=0
        for i in range(n):
            x=nums[i]
            cnt[x]+=1
            mx=max(mx,cnt[x])
            num[cnt[x]-1]-=1
            num[cnt[x]]+=1
            # 进行如下的三个判断即可
            if mx==1 and num[mx]==i+1:
                res=i
            elif num[1]==1 and num[mx]*mx==i:
                res=i
            elif num[mx]==1 and num[mx-1]*(mx-1)+num[mx]*mx==i+1:
                res=i
        return res+1

            