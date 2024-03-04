class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        st=set()
        i,j=0,0
        ans=0
        while i<n and j<n:
            while s[j] in st:
                st.remove(s[i])
                i+=1
            st.add(s[j])
            ans=max(ans,j-i+1)
            j+=1
        return ans