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

# 如果b[0] >= x,直接输出1
n, m, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
la, lb = 0, 0
cnt = 0
tot = 0
while tot < x and la < n and lb < m:
    if lb < m and tot + b[lb] >= x:
        cnt += 1
        tot += b[lb]
        lb += 1
        break
    else:
        if a[la] > 1:
            tot += a[la] * b[lb]
            la += 1
            lb += 1
            cnt += 2
        else:
            tot += b[lb]
            lb += 1
            cnt += 1
if tot >= x:
    print(cnt)
else:
    print(-1)
