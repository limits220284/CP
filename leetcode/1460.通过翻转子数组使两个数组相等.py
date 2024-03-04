class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dic=Counter(target)
        for x in arr:
            if dic[x]==0:
                return False
            else:
                dic[x]-=1
        return True
                