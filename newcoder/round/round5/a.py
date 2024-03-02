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

s = input()
s = [c for c in s]
for i, c in enumerate(s):
    if "A" <= c <= 'Z':
        s[i] = chr((ord(c) - ord('A') + 1) % 26 + ord('A'))
    if "a" <= c <= 'z':
        s[i] = chr((ord(c) - ord('a') - 1) % 26 + ord('a'))
print("".join(s))