#
# @lc app=leetcode.cn id=2434 lang=python3
#
# [2434] 使用机器人打印字典序最小的字符串
#

# @lc code=start
class Solution:
    def robotWithString1(self, s: str) -> str:
        # 考虑当前的字符，判断是不是最小的，如果是最小的
        # 直接输出即可，如果不是找到最小的则找到最小的为止
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        n = len(s)
        ans = []
        stk = []
        r = 0
        for i, c in enumerate(cnt):
            while stk and (ord(stk[-1]) - ord('a')) <= i:
                ans.append(stk[-1])
                stk.pop()
            while r < n and cnt[i] != 0:
                idx = ord(s[r]) - ord('a')
                if idx == i:
                    ans.append(s[r])
                else:
                    stk.append(s[r])
                cnt[idx] -= 1
                r += 1
        return "".join(ans)
    def robotWithString(self, s: str) -> str:
        ans = []
        cnt = Counter(s)
        min = 0  # 剩余最小字母
        st = []
        for c in s:
            cnt[c] -= 1
            while min < 25 and cnt[ascii_lowercase[min]] == 0:
                min += 1
            st.append(c)
            while st and st[-1] <= ascii_lowercase[min]:
                ans.append(st.pop())
        return ''.join(ans)
