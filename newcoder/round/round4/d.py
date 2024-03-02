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

a, b = map(int, input().split())

# 一个数的因子不会有太多
# 10 ** 9 最多也就2 ** 30次方
# 所以一个数最多30个质因子，然后通过这些质数因子来组成最终的结果，采用回溯即可，选或者不选，然后选几个的问题，最终得到的就是结果
# a * b = 2 ^ 3 4 ^ 2 5 ^ 3 7 ^ 2
# 回溯法求解即可

cnt = Counter()


def divide(x):
    i = 2
    while i <= x // i:
        if x % i == 0:
            while x % i == 0:
                x //= i
                cnt[i] += 1
        i += 1
    if x > 1:
        cnt[x] += 1


divide(a)
divide(b)
cnt = list(cnt.items())
n = len(cnt)
ans = set()


def dfs(start, tot):
    if start == n:
        ans.add(tot)
        return
    p, v = cnt[start]
    for i in range(v + 1):
        dfs(start + 1, tot * p ** i)


dfs(0, 1)
ans = sorted(list(ans))
print(len(ans))
for x in ans:
    print(x, end=" ")
