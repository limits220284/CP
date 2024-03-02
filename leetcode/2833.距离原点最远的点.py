class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left, right, ans = 0,0,0
        for c in moves:
            if c == 'L':
                left += 1
            elif c == 'R':
                right += 1
            else:
                ans += 1
        return ans + max(left, right) - min(left, right)
        