import sortedcontainers
from sortedcontainers import SortedList
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        so = SortedList()
        odd = [0] * n
        for i in range(n-1, -1, -1):
            l, r = 0, len(so)-1
            while l < r:
                mid = (l + r) // 2
                if so[mid][0] >= arr[i]:
                    r = mid
                else:
                    l = mid + 1
            if so and so[l][0] >= arr[i]:
                odd[i] = so[l][1]
            else:
                odd[i] = i
            so.add([arr[i], i])
        se = SortedList()
        even = [0] * n
        for i in range(n-1, -1, -1):
            l, r = 0, len(se)-1
            while l < r:
                mid = (l + r + 1) // 2
                if se[mid][0] <= arr[i]:
                    l = mid
                else:
                    r = mid - 1
            if se and se[l][0] <= arr[i]:
                even[i] = se[l][1]
                if arr[i] == se[l][0]:
                    se[l][1] = i
                    continue                                                                   
            else:
                even[i] = i
            se.add([arr[i], i])
        
        f = [[False, False] for _ in range(n)]
        f[-1] = [True, True]
        for i in range(n-2, -1, -1):
            if odd[i] == i:
                f[i][0] = False
            else:
                f[i][0] = f[odd[i]][1]
            if even[i] == i:
                f[i][1] = False
            else:
                f[i][1] = f[even[i]][0]
        return sum(1 if f[i][0] == True else 0 for i in range(n))