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
from bisect import *

input = lambda: sys.stdin.readline().rstrip("\r\n")

# 预处理出来10** + 7之内的所有质数
# 然后二分查找最近的质数，计算差值即可
N = int(input())
a = list(map(int, input().split()))
MX = 10 ** 5 + 7
vis = [False] * (MX + 1)
prime = []
for i in range(2, MX + 1):
    if not vis[i]:
        prime.append(i)
        j = i
        while j <= MX:
            vis[j] = True
            j += i
# print(prime)
ans = 0
for ai in a:
    idx = bisect_right(prime, ai)
    # print(prime[idx], idx)
    t = prime[idx] - ai
    if idx >= 1:
        t = min(abs(prime[idx - 1] - ai), t)
        # print("ok", t)
    ans += t
print(ans)
