class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        # 全排列一波，按着顺序排列
        # 找到最长的，判断剩下两个是不是他的子串，如果是就将其接到一起形成一个新的字符串
        # 先进行排列
        arr = [a, b, c]
        arr.sort(key = lambda x: len(x))
        a, b, c = arr[0], arr[1], arr[2]
        if a in b:
            a = b
        if a in c:
            a = c
        if b in c:
            b = c
        # print(a, b, c)
        def work(a, b, c):
            ans = ""
            # 先a和b 搞一起
            a, b, c = list(a), list(b), list(c)
            l1, l2= len(a), len(b)
            mx = 0
            for i in range(1, min(l1, l2)+1):
                if a[-i:] == b[0: i]:
                    mx = max(mx, i)
            s = a + b[mx:]

            a = s[::]
            b = c[::]
            mx = 0
            l1, l2= len(a), len(b)
            for i in range(1, min(l1, l2)+1):
                if a[-i:] == b[0: i]:
                    mx = max(mx, i)
            ans = a + b[mx:]
            return "".join(ans)
        arr = []
        arr.append(work(a, b, c))
        arr.append(work(a, c, b))
        arr.append(work(b, a, c))
        arr.append(work(b, c, a))
        arr.append(work(c, a, b))
        arr.append(work(c, b, a))
        # print(arr)
        mi = inf
        ans = None
        for s in arr:
            if len(s) < mi:
                mi = len(s)
                ans = s
            elif len(s) == mi:
                ans = min(ans, s)
        # print(ans)
                
        return ans
        
        
                    
            
        