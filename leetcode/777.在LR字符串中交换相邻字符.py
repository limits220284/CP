class Solution:
    def canTransform(self, start: str, target: str) -> bool:
        s, t = start.replace('X', ""), target.replace('X', "")
        if s != t: return False
        j = 0
        for i in range(len(start)):
            if start[i] == 'X': continue
            while target[j] == 'X': j += 1
            if start[i] == 'L' and i < j: return False
            if start[i] == 'R' and i > j: return False
            j += 1
        return True