class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        #二分答案的思路,因为答案是求最少,而且最终的结果是属于0,n之间
        #每次对于一个mid,先看从左边取是否满足,然后枚举右边,如果满足就减少mid,否则增大
        n=len(s)
        dic=Counter(s)
        # 首先判断有没有解
        if dic['a']<k or dic['b']<k or dic['c']<k:
            return -1
        
        def check(mid):
            cnt={'a':0,'b':0,'c':0}
            #先枚举左边的数字
            for i in range(mid):
                cnt[s[i]]+=1
            tot=0
            if cnt['a']>=k and cnt['b']>=k and cnt['c']>=k:
                return True
            # 减少左边,增加右边看看效果如何
            r=n-1
            for i in range(mid):
                cnt[s[mid-1-i]]-=1
                cnt[s[r-i]]+=1
                if cnt['a']>=k and cnt['b']>=k and cnt['c']>=k:
                    return True
            return False
                
        l,r=0,n
        while l<r:
            mid=(l+r)//2
            if check(mid):
                r=mid
            else:
                l=mid+1
        return l
        