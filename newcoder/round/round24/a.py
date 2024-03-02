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

n = int(input())

arr = list(range(1, n ** 2 + 1))
# print(arr)
ans = [[0] * n for _ in range(n)]
even = []
odd = []
for x in arr:
    if x % 2:
        odd.append(x)
    else:
        even.append(x)
# print(even, odd)
l, r = 0, 0
if n % 2 == 1:
    for i in range(n):
        for j in range(n):
            idx = i * n + j
            if idx % 2 == 0:
                ans[i][j] = odd[l]
                l += 1
            else:
                ans[i][j] = even[r]
                r += 1
            print(ans[i][j], end = ' ')
        print()
else:
    for i in range(n):
        for j in range(n):
            idx = i * n + j
            if idx % 2 == 0:
                ans[i][j] = odd[l]
                l += 1
            else:
                ans[i][j] = even[r]
                r += 1
    for i in range(n):
        if i % 2 == 1:
            ans[i] = ans[i][::-1]
    for i in range(n):
        for j in range(n):
            print(ans[i][j], end = ' ')
        print()