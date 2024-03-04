class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for x,y in nums1:
            dic[x]+=y
        for x,y in nums2:
            dic[x]+=y
        ans=[]
        for item in dic.items():
            ans.append(list(item))
        ans.sort()
        return ans