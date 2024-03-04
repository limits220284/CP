class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        dic=["M","P","G"]
        ans=0
        for i in range(3):
            dis=0
            for j,s in enumerate(garbage):
                if j:
                    dis+=travel[j-1]
                if dic[i] in s:
                    ans+=s.count(dic[i])
                    ans+=dis
                    dis=0
            #     print(j,ans)
            # print(i,ans)
        return ans
                