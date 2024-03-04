class Solution:
    def countEven(self, num: int) -> int:
        return (num - 1) // 2 if sum(map(int, str(num))) % 2 > 0 else num // 2
