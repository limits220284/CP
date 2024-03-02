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


def solve():
    n = int(input())
    g = [[] for _ in range(n)]
    s = input()
    IN = [0] * n
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        IN[v] += 1
        IN[u] += 1
    # print(g)
    # 寻找根节点
    ans = True
    def dfs(x, fa, red, green):
        nonlocal ans
        if s[x] == '1':
            red += 1
            green = 0
        else:
            green += 1
            red = 0
        if red >= 3 or green >= 3:
            ans = False
            return
        # print(red, green)
        for y in g[x]:
            if y != fa:
                dfs(y, x, red, green)
    # dfs(0, -1, 0, 0)
    for i in range(n):
        if IN[i] <= 2:
            dfs(i, -1, 0, 0)
    if ans:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()