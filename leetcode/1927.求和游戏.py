#
# @lc app=leetcode.cn id=1927 lang=python3
#
# [1927] 求和游戏
#

# @lc code=start
class Solution:
    def sumGame(self, num: str) -> bool:
        # Bob只有一种赢的情况，就是两边的数字相同，并且？相同
        # 否则先手必赢
        n = len(num)
        cnt1, ans1 = 0, 0
        for i in range(n // 2):
            if num[i] == '?':
                cnt1 += 1
            else:
                ans1 += int(num[i])
        l = [ans1 + cnt1 * 0, ans1 + cnt1 * 9]
        cnt2, ans2 = 0, 0
        for i in range(n // 2, n):
            if num[i] == '?':
                cnt2 += 1
            else:
                ans2 += int(num[i])
        r = [ans2 + cnt2 * 0, ans2 + cnt2 * 9]
        for i in range(cnt2 + cnt1):
            # Alice, 扩大优势，当优势无法扩大，便减少优势
            if i % 2 == 0:
                if l[0] < r[0]:
                    if cnt2 > 0:
                        r[0] += 9
                        cnt2 -= 1
                    else:
                        cnt1 -= 1
                elif l[0] > r[0]:
                    if cnt1 > 0:
                        l[0] += 9
                        cnt1 -= 1
                    else:
                        cnt2 -= 1
                else:
                    if cnt1 > cnt2:
                        l[0] += 9
                        cnt1 -= 1
                    elif cnt1 < cnt2:
                        r[0] += 9
                        cnt2 -= 1
                    else:
                        return False
            # Bob，减少优势
            else:
                if l[0] < r[0]:
                    if cnt1 > 0:
                        l[0] += 9
                        cnt1 -= 1
                    else:
                        cnt2 -= 1
                elif l[0] > r[0]:
                    if cnt2 > 0:
                        r[0] += 9
                        cnt2 -= 1
                    else:
                        cnt1 -= 1
                else:
                    if cnt1 > cnt2:
                        l[0] += 0
                        cnt1 -= 1
                    elif cnt1 < cnt2:
                        r[0] += 0
                        cnt2 -= 1
                    else:
                        return False
        return l[0] != r[0]



