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


class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n
        self.cnt = n

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.size[x] += self.size[y]
        self.p[y] = x
        self.cnt -= 1


def work(s):
    cnt = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            cnt += 1
        else:
            return cnt
    return cnt


n, m = map(int, input().split())
vals = list(map(int, input().split()))
uf = DSU(n)
edges = []
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    val = vals[x] * vals[y]
    zeros = work(str(val))
    edges.append((x, y, zeros))
edges.sort(key=lambda x: x[2])
# print(edges)
i = 0
ans = 0
for x, y, zeros in edges:
    # 尝试连接,如果连接后cnt没有变化，就不要连接
    fx, fy = uf.find(x), uf.find(y)
    if fx == fy:
        ans += zeros
    else:
        uf.union(x, y)
print(ans)
