import os
import sys

# 请在此输入您的代码

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


def even_kingdom_sort(arr):
    # 按照偶数王国规则排序：先按奇偶排序（奇数在前，偶数在后），奇偶相同时按实际数值排序
    return sorted(arr, key=lambda x: (x % 2 == 0, x))

# 示例数组
n = int(input())
a = list(map(int, input().split()))

# 输出排序后的数组

a = even_kingdom_sort(a)
for c in a:
    print(c, end=" ")

