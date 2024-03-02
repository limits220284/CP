#
# @lc app=leetcode.cn id=835 lang=python3
#
# [835] 图像重叠
#

# @lc code=start
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0
        def reverse_img(img):
            # 顺时针旋转90
            new = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    new[i][j] = img[n-1-j][i]
            return new
        def work(img1, img2):
            nonlocal ans
            for i in range(n):
                for j in range(n):
                    tot = 0
                    new = [[0] * n for _ in range(n)]
                    for x in range(n-i):
                        for y in range(n-j):
                            new[i + x][j + y] = img1[x][y]
                            if new[i+x][j+y] == 1 and img2[i+x][j+y] == 1:
                                tot += 1
                    ans = max(ans, tot)
        work(img1, img2)
        work(img2, img1)
        work(reverse_img(img1), reverse_img(img2))
        work(reverse_img(img2), reverse_img(img1))
        return ans

