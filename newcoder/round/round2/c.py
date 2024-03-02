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


col = [0] * 9
n = int(input())
for _ in range(n):
    jd, id = map(int, input().split())
    if jd == 0:
        x, y = col[id], col[id + 1]
        mx = max(x, y)
        col[id] = mx + 3
        col[id + 1] = mx + 1
    elif jd == 90:
        x, y, z = col[id], col[id + 1], col[id + 2]
        h = 0
        if x + 1 >= max(y, z):
            h = x + 2
        else:
            h = max(y, z) + 1
        col[id], col[id + 1], col[id + 2] = h, h, h
    elif jd == 180:
        x, y = col[id], col[id + 1]
        h = 0
        if y + 2 >= x:
            h = y + 3
        else:
            h = x + 1
        col[id], col[id + 1] = h, h
    else:
        x, y, z = col[id], col[id + 1], col[id + 2]
        h = max(x, y, z)
        col[id], col[id + 1], col[id + 2] = h + 1, h + 1, h + 2
for i in range(1, 9):
    print(col[i], end=" ")
