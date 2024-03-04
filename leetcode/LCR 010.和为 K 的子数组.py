class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 和为k：想到前缀和
        # 枚举右端点
        # 但是左端点怎么确定？
        # 推理->arr[r]-arr[l]=k
        # ->arr[r]-k=arr[l]
        # 只需要遍历l时候将arr[l]的值用hash表记录下来
        # 当遍历到r时候,查询hash表,如果存在dic[arr[r]-k]那么就加入即可
        # 由于枚举的是右端点,所以这种做法不会重复
        dic=Counter()
        arr=[0]
        for x in nums:
            arr.append(arr[-1]+x)
        ans=0
        for x in arr:
            if x-k in dic:
                ans+=dic[x-k]
            dic[x]+=1
        return ans


            
