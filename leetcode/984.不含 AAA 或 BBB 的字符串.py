class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        # 根据鸽巢原理,小的那一方作为隔板,一共划分b+1个盒子
        # 如果出现某一方一定有三个的话，必定存在2(b+1)+1个a,否则不可能
        # 思路:首先建立b+1个盒子
        # 如果a>=b+1,那么b+1个盒子里必然出现一个a
        # a<b 的情况直接将a换成b,b换成a即可
        x,y=a,b
        if a<b:
            a,b=b,a
        d=a//(b+1)
        m=a%(b+1)
        arr=[d]*(b+1)
        for i in range(m):
            arr[i]+=1
        ans=[]
        for i in arr:
            for j in range(i):
                ans.append('a')
            ans.append('b')
        if x<y:
            for i,c in enumerate(ans):
                ans[i]='a' if c=='b' else 'b'
        return "".join(ans[:-1])
            
