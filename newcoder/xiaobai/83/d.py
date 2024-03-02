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
from math import inf

input = lambda: sys.stdin.readline().rstrip("\r\n")

MOD = 998244353
n = int(input())
s = input()
m = int(input())

MX = 510
fac = [0] * MX
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_fac = [0] * MX
inv_fac[MX - 1] = pow(fac[MX - 1], MOD - 2, MOD)
for i in range(MX - 1, 0, -1):
    inv_fac[i - 1] = inv_fac[i] * i % MOD


def comb(n: int, k: int) -> int:
    return fac[n] * inv_fac[k] % MOD * inv_fac[n - k] % MOD


f = [[[0] * 501 for _ in range(26)] for _ in range(26)]


def INIT():
    for i in range(n):
        for j in range(i + 1, n):
            l = j - i + 1
            for k in range(2, l + 1):
                f[ord(s[i]) - ord("a")][ord(s[j]) - ord("a")][k] = (
                    f[ord(s[i]) - ord("a")][ord(s[j]) - ord("a")][k]
                    + comb(l - 2, k - 2)
                ) % MOD


INIT()
for _ in range(m):
    query = input().split()
    be, ed, length = ord(query[0]) - ord("a"), ord(query[1]) - ord("a"), int(query[2])
    print(f[be][ed][length])
