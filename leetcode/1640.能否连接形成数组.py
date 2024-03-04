class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic=defaultdict(int)
        for i,x in enumerate(arr):
            dic[x]=i
        for ar in pieces:
            n=len(ar)
            if n==1:
                if ar[0] not in dic:
                    return False
            else:
                for i in range(1,n):
                    if dic[ar[i-1]]!=dic[ar[i]]-1:
                        return False
        return True
            
