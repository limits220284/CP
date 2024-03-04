class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        #出现子序列，划分，相邻这种字眼一般都是动态规划问题
        f=[0]*26
        for c in s:
            i=ord(c)-ord('a')
            f[i]=max(f[max(0,i-k):min(i+k,25)+1])+1
        return max(f)