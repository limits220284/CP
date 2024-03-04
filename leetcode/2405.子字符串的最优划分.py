class Solution:
    def partitionString(self, s: str) -> int:
        st=set()
        cnt=0
        for c in s:
            if c not in st:
                st.add(c)
            else:
                cnt+=1
                st=set()
                st.add(c)
        if st:
            cnt+=1
        return cnt