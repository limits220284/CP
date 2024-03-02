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


def solve():
    X, S, Y = input().split()
    X = int(X)
    Y = int(Y)
    if S == "KB":
        X = 1024 * X
    elif S == "MB":
        X = 1024 * 1024 * X
    print(X // Y)
T = int(input())
for _ in range(T):
    solve()