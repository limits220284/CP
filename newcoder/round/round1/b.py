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
a = list(map(int, input().split()))
color = [c for c in input()]
cnt = defaultdict(list)
for ai, colori in zip(a, color):
    cnt[ai].append(colori)
print(cnt)
ans = 0
for _, v in cnt.items():
    r, b = 0, 0
    for c in v:
        if c == "R":
            r += 1
        else:
            b += 1
    ans += r * b
print(ans)
