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

n, h, k = map(int, input().split())
monster = [[0, 0] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    monster[i] = [a, b]
needs = []
for i, [a, b] in enumerate(monster):
    need = 0
    circle = a // 4
    need = circle * 3
    rest = a % 4
    if rest != 0:
        need += 1 if rest <= 2 else 2
    needs.append((need - 1) * b)
needs.sort()
prefix = [0]
for x in needs:
    prefix.append(prefix[-1] + x)
q = int(input())
qv = list(map(int, input().split()))
ans = [0] * q
for i in range(q):
    x = qv[i]
    up = h + x * k
    left = bisect.bisect_left(prefix, up)
    print(left - 1, end = " ")

