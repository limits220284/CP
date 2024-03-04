class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word+='#'
        n=len(word)
        pre=0
        cnt=0
        st=set()
        i=0
        while i<n:
            if word[i].isdigit():
                j=i
                while word[i].isdigit():
                    i+=1
                st.add(int(word[j:i]))
            i+=1
        return len(st)
            
                
                