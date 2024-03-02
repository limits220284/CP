class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        # 就是哪里放逗号，哪里放点的问题
        s = s[1: -1]
        n = len(s)
        def check(ss):
            if "." not in ss:
                if len(ss) > 1 and ss[0] == '0':
                    return False
                return True
            else:
                idx = ss.index(".")
                if idx == 0:
                    return False
                if ss[-1] == '0': return False
                ss = ss[:idx]
                if len(ss) > 1 and ss[0] == '0':
                    return False
                return True

        ans = []
        for i in range(1, n):
            for j in range(i):
                s1 = s[:j + 1] + "." + s[j + 1: i]
                if s1[-1] == ".": s1 = s1[: -1]
                for k in range(i, n):
                    s2 = s[i: k + 1] + "." + s[k + 1:]
                    if s2[-1] == ".": s2 = s2[: -1]
                    if check(s1) and check(s2):
                        ans.append("(" + s1 + ", " + s2 + ")")
        return ans