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

import sys


def solve(s, t) -> int:
    n = len(s)
    s1 = [i for i in range(n) if s[i] == "1"]
    t1 = [i for i in range(n) if t[i] == "1"]
    ans = 0
    for si, ti in zip(s1, t1):
        ans += abs(si - ti)
    return ans


s0 = sys.stdin.readline().strip()
c0 = s0.count("0")
c1 = s0.count("1")
if c0 == c1:
    print(min(solve(s0, "01" * c0), solve(s0, "10" * c0)))
elif c0 < c1:
    print(solve(s0, "10" * c0 + "1"))
else:
    print(solve(s0, "01" * c1 + "0"))
