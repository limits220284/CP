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


n, k, x = map(int, input().split())
mi, mx = (1 + n) * n // 2, (k + k - n + 1) * n // 2
print(mi, mx)
if n > k or not(mi <= x <= mx):
    print(-1)
else:
    diff = x - mi
    circle = diff // n
    rest = circle % n
    ans = list(range(1, n + 1))
    print(ans)
    for i in range(n):
        ans[i] += circle
    for i in range(n - 1, -1, -1):
        if rest <= 0:
            break
        ans[i] += 1
        rest -= 1
    for x in ans:
        print(x, end = " ")
