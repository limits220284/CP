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

# 贪心一下即可
# 只保留一位小数点剩下的都搞成数字

s = input()
n = len(s)

i = 0
start = 0
ans = 0
while i < n:
    if s[i] == ".":
        ans += float(s[start : i + 2])
        print(float(s[start : i + 2]))
        i += 2
        start = i
    else:
        i += 1
ans += float(s[start:])
