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
    # 如果是质数，直接返回自己
    # 如果不是质数，直接从1-1e6枚举p，找到了就直接返回
    n = int(input())
    up = int(math.sqrt(n - 0.000000001))
    print(up)
    flag = False
    for i in range(up, 1, -1):
        if n % i == 0:
            flag = True
            print(n // i)
            break
    if flag == False:
        print(n)
    print()


t = int(input())
for _ in range(t):
    solve()