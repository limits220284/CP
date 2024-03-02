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
from math import *
input = lambda: sys.stdin.readline().rstrip("\r\n")

# 枚举最终要变成字母是什么，然后判断需要多少次即可
s = input()
ans = inf
for i in range(26):
    tar = chr(i + ord('a'))
    print(tar)
    cnt = 0
    for _, c in enumerate(s):
        x = ord(c) - ord('a')
        mi = (x - i) % 26
        mi = min(mi, 26 - mi)
        cnt += mi
    ans = min(cnt, ans)
print(ans)