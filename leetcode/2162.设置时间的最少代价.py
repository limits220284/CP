class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        # 直接枚举所有的可能性,即先枚举分钟数,然后计算秒数是否可行
        mx_minute = targetSeconds // 60 + 1 #最多的分钟数
        arr = []
        for minute in range(mx_minute):
            second = targetSeconds - minute * 60
            if second > 99 or minute > 99:
                continue
            else:
                # 计算需要花费,多的不如少的好
                a = str(minute)
                b = str(second)
                if a == '0':
                    a = ''
                elif len(a) <= 2:
                    if len(b) < 2:
                        b = '0' + b
                arr.append(a + b)
        ans = 1e9
        for t in arr:
            tot = 0
            n = len(t)
            pre = str(startAt)
            for i in range(n):
                if t[i] != pre:
                    tot += moveCost
                    pre = t[i]
                tot += pushCost
            ans = min(tot, ans)
        return ans