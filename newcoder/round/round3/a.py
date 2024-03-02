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


s = [c for c in input()]
n = len(s)


def check(x):
    if x % 7 == 0:
        return True
    return False


# 直接枚举所有的情况
ans = 0
for i in range(n + 1):
    for j in range(10):
        if i == 0 and j == 0:
            continue
        t = str(j)
        x = "".join(s[:i] + [t] + s[i:])
        if check(int(x)):
            ans = int(x)
            break
print(ans)
