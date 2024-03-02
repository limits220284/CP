class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s, t = start.replace('_', ""), target.replace('_', "")
        print(s, t)
        if s != t: return False
        j = 0
        for i in range(len(start)):
            if start[i] == '_': continue
            while target[j] == '_': j += 1
            if start[i] == 'L' and i < j: return False
            if start[i] == 'R' and i > j: return False
            j += 1
        return True
        