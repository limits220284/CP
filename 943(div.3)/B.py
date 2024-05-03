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

T = int(input())

def solve():
    n, m = map(int, input().split())
    a = input()
    b = input()
    def check(mid):
        i, j = 0, 0
        while i < mid and j < m:
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == mid
    l, r = 0, n
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(l)
for _ in range(T):
    solve()