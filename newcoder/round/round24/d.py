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


# 一眼二分答案
n, k, x = map(int, input().split())
a = list(map(int, input().split()))

def check(mid):
    cnt = 0
    for y in a:
        if y <= mid:
            continue
        else:
            cnt += math.ceil((y - mid) / x)
    return cnt <= k
mx = 10 ** 18
l, r = -mx, max(a)
while l < r:
    mid = (l + r + 1) // 2
    if check(mid) == False:
        l = mid
    else:
        r = mid - 1
print(l + 1)