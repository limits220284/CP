class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set([tuple(x) for x in queens])
        ans = []
        for inx, iny in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            x, y = king[0] + inx, king[1] + iny
            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in queens:
                    ans.append([x, y])
                    break
                x += inx
                y += iny
        return ans
                
                