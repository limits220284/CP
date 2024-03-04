class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        return 1 if not presses else (2 if n == 1 else ((4 if presses == 1 else (7 if presses == 2 else 8)) if n > 2 else (3 if presses == 1 else 4)))