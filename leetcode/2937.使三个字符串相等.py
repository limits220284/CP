class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        ptr = 0
        n1,n2,n3 = len(s1),len(s2),len(s3)
        minn = min(n1,n2,n3)
        while ptr < minn and s1[ptr]==s2[ptr] and s2[ptr] == s3[ptr]:
            ptr+=1
        if ptr == 0:
            return -1
        return (len(s1)+len(s2)+len(s3)-3 * ptr)
            