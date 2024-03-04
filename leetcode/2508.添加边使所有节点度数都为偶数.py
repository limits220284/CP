class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        dic={}
        # 先统计一下每个点的出度和入度
        d=[0]*(n+1)
        for x,y in edges:
            dic[(x,y)]=True
            dic[(y,x)]=True
            d[x]+=1
            d[y]+=1
        cnt=0
        ans=[]
        for i,x in enumerate(d):
            if x%2==1:
                cnt+=1
                ans.append(i)
        if cnt>4:
            return False
        if cnt%2==1:
            return False
        if cnt==2:
            if (ans[0],ans[1]) not in dic:
                return True
            for i in range(1,n+1):
                if i!=ans[0] and i!=ans[1] and (ans[0],i) not in dic and (ans[1],i) not in dic:
                    return True
            return False
        if cnt==4:
            for i in range(3):
                for j in range(i+1,4):
                    t=[]
                    for k in range(4):
                        if k!=i and k!=j:
                            t.append(k)
                    if (ans[i],ans[j]) not in dic and (ans[t[0]],ans[t[1]]) not in dic:
                        return True
            return False
        return True
            