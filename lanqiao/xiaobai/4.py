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

# lowbit(ai + aj) = ai + aj
# 表示他俩相同或者他俩相加是2的幂次方
# 所以可以通过一个hash表来解决问题
# 数字范围1e9，32位足够
n = int(input())
a = list(map(int, input().split()))
st = defaultdict(int)
ans = 0
for i in range(n):
    for j in range(33):
        tar = 1 << j
        # print(tar, tar - a[i])
        if tar - a[i] in st:
            # print(tar, tar - a[i])
            ans += st[tar - a[i]]
    st[a[i]] += 1
print(ans)