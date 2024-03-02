class Solution:
    def maximizeWin(self, pos: List[int], k: int) -> int:
        # "两个这种词语" ->直接想到两数之和，枚举后面一个，然后记录前面一个线段的最大值
        # 有一种动态规划的思想,pre[i] 保存的一直都是i左边长度为 2 的线段中奖品数量的最大值。
        n = len(pos)
        pre = [0] * (n + 1)
        left = 0
        ans = 0
        for right, p in enumerate(pos):
            while p - pos[left] > k:
                left += 1
            ans = max(ans, right - left + 1 + pre[left])
            pre[right + 1] = max(pre[right], right - left + 1)
        return ans