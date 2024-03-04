class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        a=0
        n=len(words)
        while True:
            if words[(startIndex+a) % n]==target:
                break
            a+=1
        b=0
        while True:
            if words[(startIndex - b + n) % n]==target:
                break
            b+=1
        return min(a,b)
        