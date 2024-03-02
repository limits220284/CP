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
from bisect import *
from math import *

input = lambda: sys.stdin.readline().rstrip("\r\n")

N = 100010
now = [0] * N
now[0] = 1
m = 1
while True:
    now[m] = now[m - 1] // gcd(now[m - 1], m) * m
    if now[m] > 10 ** 16:
        break
    m += 1


def solve():
    a, n = map(int, input().split())
    if a > m:
        print(0)
    else:
        print(n // now[a - 1] - n // now[a])


t = int(input())
for _ in range(t):
    solve()
