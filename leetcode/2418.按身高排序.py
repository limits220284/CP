class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr=list(zip(names,heights))
        arr.sort(key=lambda x:x[1],reverse=True)
        ans=[]
        for x in arr:
            ans.append(x[0])
        return ans