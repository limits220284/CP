class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.ceil(sqrt(n+1)-1)
        # n<=(i+1)**2-1
        