class Solution:
    def countVowels(self, word: str) -> int:
        # 动态规划求解
        # f[i] 代表的是以 word[i] 结尾的子串包含元音的个数
        # 如果当前字符为 元音,那么必定在 以 word[i-1] 结尾的元音个数后面加了一个i+1
        n=len(word)
        f=[0]*(n+1)
        dic={'a','e','i','o','u'}
        for i,ch in enumerate(word):
            if ch in dic:
                f[i+1]=f[i]+i+1
            else:
                f[i+1]=f[i]
        return sum(f)