class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        st=set()
        i,j=0,0
        ans=0
        while i<n and j<n:
            if i!=0:
                st.remove(s[i-1])
            while j<n and s[j] not in st:
                st.add(s[j])
                j+=1
            ans=max(ans,j-i)
            i+=1
        return ans