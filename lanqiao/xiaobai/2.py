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

s1 = input()
s2 = input()
n = len(s1)
def segment_changes(s1, s2):
    # 定义每个数字对应的七段显示的二进制表示
    segment_map = {
        '0': 0b0111111,
        '1': 0b0000110,
        '2': 0b1011011,
        '3': 0b1001111,
        '4': 0b1100110,
        '5': 0b1101101,
        '6': 0b1111101,
        '7': 0b0000111,
        '8': 0b1111111,
        '9': 0b1101111
    }

    # 计算变化量
    total_changes = 0
    for digit_s1, digit_s2 in zip(s1, s2):
        # 计算两个数字之间的线段差异
        changes = segment_map[digit_s1] ^ segment_map[digit_s2]
        # 计数差异中的1的个数（即变化的线段数）
        total_changes += bin(changes).count('1')

    return total_changes

# 计算从s1到s2的变化量
t = segment_changes(s1, s2)
print(t)