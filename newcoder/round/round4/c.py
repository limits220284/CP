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


MOD = 10 ** 9 + 7

n, k = map(int, input().split())
stk = []
a = list(map(int, input().split()))
for _ in range(k):
    op, x = map(int, input().split())
    if op == 1:
        # 加
        if not stk:
            stk.append(x)
        else:
            if stk[-1] < 0:
                stk.append(x)
            else:
                stk[-1] += x
    if op == 2:
        # 减
        if not stk:
            stk.append(-x)
        else:
            if stk[-1] < 0:
                stk[-1] -= x
            else:
                if stk[-1] >= x:
                    stk[-1] -= x
                    if stk[-1] == 0:
                        stk.pop()
                else:
                    stk[-1] = - (x - stk[-1])
                    cnt = 0
                    while stk and stk[-1] < 0:
                        cnt += abs(stk.pop())
                    stk.append(-cnt)
print(stk)
for x in stk:
    for i in range(n):
        if x > 0:
            a[i] += x
        else:
            a[i] = max(a[i] + x, 0)

print(sum(a) % MOD)