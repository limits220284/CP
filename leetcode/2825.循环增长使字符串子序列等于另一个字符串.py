class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n1 = len(str1)
        n2 = len(str2)
        j = 0
        for i in range(n1):
            c1 = str1[i]
            c2 = chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a'))
            # print(c1, c2)
            if str2[j] == c1 or str2[j] == c2:
                j += 1
            if j == n2:
                return True
        return False
        