import heapq
import time
import bisect
import functools
import math
import os
import random
import re
import sys
import threading
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from io import BytesIO, IOBase
from itertools import accumulate, combinations, permutations
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase
from typing import *
input = lambda: sys.stdin.readline().rstrip("\r\n")
# 如果k-1都必须要击败的话，那么第k个一定是最低的，或者说后续的一定是最低的，不然我完全可以一直搞前面的
# 首先就是不搞怪兽之王，没必要搞它，因为前面的足够了，那就是每次都选最小的即可
# 要么就可以搞怪兽之王，如果搞怪兽之王，那么需要先搞完前k-1个，然后再搞怪兽之王，然后不够的话，继续从堆里取出来最小的
# 不搞的话，可以直接从前面的堆里一直取即可
# 然后二分最小值
# 可以二分最后的结果
h = []
k, n = map(int, input().split())
a = []
for _ in range(k):
    t = list(map(int, input().split()))
    a.append(t)

def check_not_have(mid):
    h = []
    for i in range(k - 1):
        heappush(h, (a[i][0], a[i][1]))
    cnt = 0
    while True:
        x, y = h[0]
        if mid >= x:
            mid -= x
            cnt += 1
        else:
            return False
        if cnt >= n:
            return True
        heappop(h)
        heappush(h, (y, y))


def check_have(mid):
    h = []
    for i in range(k - 1):
        mid -= a[i][0]
    cnt = k - 1
    if mid < 0:
        return False
    for i in range(k - 1):
        heappush(h, (a[i][1], a[i][1]))
    heappush(h, (a[k - 1][0], a[k - 1][1]))
    while True:
        if cnt >= n:
            return True
        x, y = h[0]
        if mid >= x:
            mid -= x
            cnt += 1
        else:
            return False
        heappop(h)
        heappush(h, (y, y))

def check(mid):
    flag1 = check_not_have(mid)
    if flag1:
        return True
    flag2 = check_have(mid)
    return flag2 or flag1

# l, r = 0, int(1e15)
# while l < r:
#     mid = (l + r) // 2
#     if check(mid):
#         r = mid
#     else:
#         l = mid + 1
# print(l)
ans = bisect.bisect_left(range(1e15), True, key=check)