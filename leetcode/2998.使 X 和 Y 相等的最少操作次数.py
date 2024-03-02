class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x <= y:
            return y - x
        h = [x]
        vis = set()
        minn = x - y
        mxt = max((x // 11 + 1) * 11, (x // 5 + 1) * 5)
        mnt = min((x // 11) * 11, (x // 5) * 5)
        ct = 0
        while len(h):
            s = []
            if ct >= minn:
                break
            for v in h:
                if v <= y:
                    minn = min(minn, ct + y - v)
                    continue
                if v %11==0:
                    if v //11 in vis:
                        continue
                    vis.add(v // 11)
                    s.append(v // 11)
                if v % 5 == 0:
                    if v // 5 in vis:
                        continue
                    vis.add(v // 5)
                    s.append(v // 5)
                if v > mxt:
                    continue
                if v + 1 not in vis:
                    s.append(v + 1)
                    vis.add(v + 1)
                if v -1 not in vis:
                    s.append(v - 1)
                    vis.add(v - 1)
            h = s
            ct += 1    
        return minn