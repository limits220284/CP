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
from fractions import Fraction as frac

input = lambda: sys.stdin.readline().rstrip("\r\n")

MOD = 998244353
N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))


def div(a, b):
    return a * pow(b, -1, MOD) % MOD


ps = sum(div(x, y) for x, y in zip(a, b)) % MOD
qs = sum(div(x, y) for x, y in zip(a, b)) % MOD
ans = N * (ps + qs) - 2 * ps * qs

ans %= MOD
print(ans)
