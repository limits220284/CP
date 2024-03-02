class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        l = min(nums)
        r = max(nums)
        dic =defaultdict(int)
        nums.sort()
        for num in nums:
            dic[num]+=1
        to = defaultdict(int)
        for k,d in dic.items():
            if k-1 in dic:
                to[k]=to[k-1]+1
            else:
                to[k]=1
        mxn = 1
        ptr = l-1
        for i in range(l,r+3):
            if dic[i] == 0 and dic[i-1]<2:
                mxn = max(i-1-ptr+to[ptr-1],mxn)
                ptr = i
                continue
            if dic[i-1]>=2:
                dic[i]+=1
        return mxn