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

MOD = 10 ** 9 + 7

s = [int(c) for c in input()]
n = len(s)
f = [[0] * 9 for _ in range(n + 1)]
# f[i]表示前i个数字构成是9的倍数的子序列的和
# 和也是9的倍数，需要记录和mod9的余数
# f[i][j]表示前i个数选出子序列和mod9为j的数量 j 属于0-8
# f[i][j] = f[i - 1][j] + f[i - 1][(j + nums[i]) % 9]
# 刷表法
# f[i][(j + nums[i]) % 9] += f[i][j] + f[i - 1][(j + nums[i]) % 9]
f[0][0] = 1
for i in range(1, n + 1):
    for j in range(10):
        f[i][(j + s[i - 1]) % 9] = f[i - 1][j] + f[i - 1][(j + s[i - 1]) % 9]
print(f[n][0] - 1)
