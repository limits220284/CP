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

t = int(input())


def solve():
    a, b, c = map(int, input().split())
    pa, pb, pc = a / 16, b / 16, c / 16
    p12tong = pa ** 12
    pdesk = pb ** 4 + pc ** 4
    pans = 1820 * p12tong * pdesk + pa ** 16
    print(round(pans, 11))


for _ in range(t):
    solve()
