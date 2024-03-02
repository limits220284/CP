class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        m = defaultdict(list)
        for allow in allowed:
            m[allow[:2]].append(allow[2])
        def helper(s):
            p = []
            for i in range(1, len(s)):
                chs = m[s[i - 1] + s[i]]
                if len(chs) == 0: return False
                p.append(chs)
            if len(p) == 1: return True
            for chs in product(*p):
                if helper("".join(chs)):
                    return True

            return False
        return helper(bottom)