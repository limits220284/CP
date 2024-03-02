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

A, B, S, T = map(int, input().split())
def it(A, B, T):
    if T < 0:
        return 0
    res = 0
    for i in range(1, B + 1):
        # 计算A是i的多少倍
        p = A // i
        f = min(i - 1, T) + 1
        # 计算一下mod后，必须小于T，不能超过T，也不能超过i - 1
        # 0 - min(i - 1, T)一共+1个数
        # 每一轮的A都算在里面
        res += f * p
        # 看余数
        p = A % i
        # 余数也必须小于等于T，这里不加1，是因为最后一个零这个部分被计算了两次
        res += min(p, T)
    return res

print(it(A, B, T) - it(A, B, S - 1))