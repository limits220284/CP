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

# 贪心构造题目
# 中间放置的是最多的数
# 假设k > n - k
# 中间的数为2
# 剩余k - 1个2，n - k个三
n, k = map(int, input().split())
mx, mi = max(k, n - k), min(k, n - k)
MOD = 10 ** 9 + 7
ans = 1
ans = ans * pow(3, mx - 1, MOD) * pow(4, mi, MOD) % MOD
ans = (
    ans
    * pow(4, (mx - 1) * (mx - 2) // 2, MOD)
    * pow(6, (mx - 1) * mi + mi * (mi - 1) // 2, MOD)
    % MOD
)
print(ans % MOD)
