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

n, k = map(int, input().split())
a = [0] * n
for i in range(k):
    a[i * 2] = n - k + i + 1

i = 0
j = 0
while i < n - k:
    while j < n and  a[j] != 0:
        j += 1
    a[j] = n - k - i
    i += 1

for x in a:
    print(x, end = " ")