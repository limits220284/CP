class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        al=[0]
        mx=0
        for x in gain:
            al.append(x+al[-1])
        return max(al)