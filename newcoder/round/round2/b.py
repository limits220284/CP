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

n = int(input())
a = list(map(int, input().split()))
color = input()
# 定义f[i]表示前i个能够获得的最大分数
# 当前这个数标记还是不标记
# 如果和左边的相同，只能不标记，然后取前面的最大值
# 如果和左边的不同，可以不标记，f[i-1], 标记f[i] = cnt1 + cnt2 + f[i - 2]
f = [0] * (n + 1)
for i in range(2, n + 1):
    f[i] = f[i - 1]
    if color[i - 1] != color[i - 2]:
        f[i] = max(f[i], f[i - 2] + a[i - 1] + a[i - 2])
print(f[-1])
