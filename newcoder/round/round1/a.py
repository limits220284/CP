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

for i in range(3 * n):
    for j in range(n):
        print("*", end="")
    for j in range(n, 3 * n):
        print(".", end="")
    for j in range(3 * n, 4 * n):
        print("*", end="")
    print()
for i in range(n):
    for j in range(i + 1):
        print(".", end="")
    for j in range(n):
        print("*", end="")
    for j in range(4 * n - 2 * n - 2 * (i + 1)):
        print(".", end="")
    for j in range(n):
        print("*", end="")
    for j in range(i + 1):
        print(".", end="")
    print()
