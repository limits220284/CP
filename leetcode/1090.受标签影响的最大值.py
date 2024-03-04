class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        #贪心算法即可
        res=0
        mp=list(zip(values,labels))
        mp.sort(reverse=True)
        dic=defaultdict(int)
        cnt=0
        for x in mp:
            if dic[x[1]]<useLimit:
                dic[x[1]]+=1
                res+=x[0]
                cnt+=1
            else:
                continue
            if cnt==numWanted:
                break
        return res