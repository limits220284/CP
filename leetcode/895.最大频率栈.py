#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#

# @lc code=start
class FreqStack:
    # 太妙了
    def __init__(self):
        self.cnt = Counter()
        self.stk = defaultdict(list)
        self.mx = 0
    def push(self, val: int) -> None:
        self.cnt[val] += 1
        self.stk[self.cnt[val]].append(val)
        self.mx = max(self.mx, self.cnt[val])
    def pop(self) -> int:
        k = self.stk[self.mx].pop()
        self.cnt[k] -= 1
        if len(self.stk[self.mx]) == 0:
            self.mx -= 1
        return k
        

