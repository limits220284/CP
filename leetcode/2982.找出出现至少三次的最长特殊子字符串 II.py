class Solution:
    def maximumLength(self, s: str) -> int:
        ct = 1
        n = len(s)
        dic = defaultdict(list)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                ct += 1
            else:
                dic[s[i - 1]].append(ct)
                ct = 1
        dic[s[-1]].append(ct)
        mxn = -1
        for k, d in dic.items():
            d.sort()
            if len(d) == 1:
                if d[0] >= 3:
                    mxn = max(mxn, d[0] - 2)
            elif len(d) == 2:
                if d[-1] == 1:
                    continue
                if d[-1] > d[-2]:
                    mxn = max(mxn, d[-1] - 2, d[-2])
                else:
                    mxn = max(mxn, d[-1] - 1)
            else:
                if d[-1] == d[-2]:
                    if d[-2] == d[-3]:
                        mxn = max(mxn, d[-1])
                    else:
                        mxn = max(mxn, d[-1] - 1)
                else:
                    mxn = max(mxn, d[-1] - 2, d[-2])
        return mxn