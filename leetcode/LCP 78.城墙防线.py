class Solution:
    def rampartDefensiveLine(self, ra: List[List[int]]) -> int:
        # 二分查找
        # 先预处理出来所有的线段
        arr = []
        n = len(ra)
        for i in range(n-1):
            arr.append(ra[i+1][0] - ra[i][1])
        m = n-1
        tot = sum(arr)
        def check(mid):
            ar = arr[::] # 复制一份
            # 共len(arr) 个间隔,要保证len(arr)-1个mid长度的扩张都能够成立
            if mid * (m-1) > tot:
                return False
            for i in range(m-1):
                if mid > ar[i] + ar[i+1]:
                    return False
                if mid > ar[i]:
                    ar[i+1] -= (mid - ar[i])
                    ar[i] = 0
                else:
                    ar[i] -= mid
            return True

                # if ar[i] >= mid:
                #     ar[i] -= mid
                #     mid = 0
                #     continue
                # else:
                #     mid -= ar[i]
                #     ar[i] = 0
                # if ar[i+1] >= mid:
                #     ar[i+1] -= mid
                #     mid = 0
                #     continue
                # else:
                #     mid -= ar[i+1]
                #     ar[i+1] = 0
                #     return False
                
        l, r = 0, 10 ** 8
        while l < r:
            mid = (l+r+1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l