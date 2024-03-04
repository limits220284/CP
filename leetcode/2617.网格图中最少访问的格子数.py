class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        # 动态规划+单调栈+二分
        m, n = len(grid), len(grid[0])
        col_st = [[] for _ in range(n)]

        def search(st, i):
            # l, r = 0, len(st)-1
            # while l < r:
            #     mid = (l + r + 1) // 2
            #     if st[mid][1] <= i:
            #         l = mid
            #     else:
            #         r = mid - 1
            # return l
            l, r = -1, len(st)
            while l + 1 < r:
                mid = (l + r) // 2
                if st[mid][1] <= i:
                    r = mid
                else:
                    l = mid
            return r
            
        for i in range(m-1, -1, -1):
            row = grid[i]
            st = []
            for j in range(n-1, -1, -1):
                st2 = col_st[j]
                mn = inf
                g = row[j]
                if i == m-1 and j == n-1:
                    mn = 0
                elif g:
                    k = j + g
                    k = search(st, k)
                    if k < len(st):
                        mn = min(mn, st[k][0])

                    k = i + g
                    k = search(st2, k)
                    if k < len(st2):
                        mn = min(mn, st2[k][0])
                if mn < inf:
                    mn += 1
                    while st and mn <= st[-1][0]:
                        st.pop()
                    st.append((mn, j))

                    while st2 and mn <= st2[-1][0]:
                        st2.pop()
                    st2.append((mn, i))
        return mn if mn < inf else -1
