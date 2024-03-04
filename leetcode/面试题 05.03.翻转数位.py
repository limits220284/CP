class Solution:
    def reverseBits(self, num: int) -> int:
        i=0
        pre,cur=0,0
        mx=-1
        while i<32:
            if num&1<<i:
                pre+=1
                cur+=1
            else:
                #mx=max(mx,pre)
                pre=cur+1
                cur=0
            i+=1
            mx=max(mx,pre)
           
        return mx
