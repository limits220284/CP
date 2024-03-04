class Solution:
    def countDistinct(self, nums: List[int], k: int, md: int) -> int:
        Trie={}
        st=set()
        def insert(l,r):
            p=Trie
            while l<r:
                p=p.setdefault(nums[l],{})
                if nums[l]%md==0:
                    p['count']=1
                l+=1
        def query(l,r):
            p=Trie
            cnt=0
            i=l
            while i<r:
                if nums[i] not in p:
                    return
                p=p[nums[i]]
                cnt+=p.get('count',0)
                if cnt<=k:
                    st.add(str(nums[l:i+1]))
                i+=1
        n=len(nums)
        for i in range(n):
            insert(i,n)
        for i in range(n):
            query(i,n)
        return len(st)
        