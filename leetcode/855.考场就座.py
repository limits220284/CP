from sortedcontainers import *
class Region:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __lt__(self, other):
        d1, d2 = self.second - self.first, other.second - other.first
        return d1 // 2 > d2 // 2 or (d1 // 2 == d2 // 2 and self.first < other.first)
class ExamRoom1:

    def __init__(self, n: int):
        self.n = n
        self.seats = SortedList()
        self.pq = []

    def seat(self) -> int:
        seats, pq, n = self.seats, self.pq, self.n
        if not seats:
            seats.add(0)
            return 0
        left, right = seats[0], n - 1 - seats[-1]                                                            # 最左，最右空的座位数
        while len(seats) >= 2:
            p = pq[0]
            if p.first in seats and p.second in seats and seats.index(p.first) + 1 == seats.index(p.second): # 不属于延迟删除的区间,中间没有其他的数字
                d = p.second - p.first
                if d // 2 <= left or d // 2 < right: break                                                      # 最左或者最右的座位更优
                p = heappop(pq)
                heappush(pq, Region(p.first, p.first + d // 2))
                heappush(pq, Region(p.first + d // 2, p.second))
                seats.add(p.first + d // 2)
                return p.first + d // 2
            heappop(pq)
        if right > left:
            heappush(pq, Region(seats[-1], n - 1))
            seats.add(n - 1)
            return n - 1
        else:
            heappush(pq, Region(0, seats[0]))
            seats.add(0)
            return 0

    def leave(self, p: int) -> None:
        seats, pq = self.seats, self.pq
        if p != seats[0] and p != seats[-1]:
            idx = seats.index(p)
            heappush(pq, Region(self.seats[idx - 1], self.seats[idx + 1]))
        seats.remove(p)
class ExamRoom:

    def __init__(self, n: int):
        # 离散化处理
        self.st = SortedList()
        self.h = []
        self.n = n
        
    def seat(self) -> int:
        if len(self.st) == 0:
            self.st.add(0)
            return 0
        elif len(self.st) == 1:
            idx = self.st[0]
            if idx == 0:
                self.st.add(self.n-1)
                heappush(self.h, Region(0, self.n-1))
                return self.n - 1
            elif idx == self.n - 1:
                self.st.add(0)
                heappush(self.h, Region(0, self.n-1))
                return 0
            else:
                if idx >= self.n-1 - idx:
                    self.st.add(0)
                    heappush(self.h, Region(0, idx))
                    return 0
                else:
                    self.st.add(self.n-1)
                    heappush(self.h, Region(idx, self.n-1))
                    return self.n-1
        else:
            pre = self.st[0]
            last = self.n-1 - self.st[-1]
            while True:
                p = self.h[0]
                l, r = p.first, p.second
                # 判断当前的区间是否合理，如果不合理直接删除
                if l not in self.st or r not in self.st or (self.st.index(l) + 1) != self.st.index(r):
                    heappop(self.h)
                    continue
                dis = p.second - p.first
                if dis//2 > max(pre, last):
                    heappop(self.h)
                    self.st.add(l + dis//2)
                    heappush(self.h, Region(l, l + dis//2))
                    heappush(self.h, Region(l + dis//2, r))
                    return l + dis//2
                elif dis//2 == max(pre, last):
                    if dis//2 == pre:
                        self.st.add(0)
                        heappush(self.h, Region(0, pre))
                        return 0
                    elif dis//2 == last:
                        heappop(self.h)
                        self.st.add(l + dis//2)
                        heappush(self.h, Region(l, l + dis//2))
                        heappush(self.h, Region(l + dis//2, r))
                        return l + dis//2
                else:
                    if pre >= last:
                        self.st.add(0)
                        heappush(self.h, Region(0, pre))
                        return 0
                    else:
                        self.st.add(self.n-1)
                        heappush(self.h, Region(self.n-1-last, self.n-1))
                        return self.n-1
                break

    def leave(self, p: int) -> None:
        # 删除该点并且合并两个区间
        if (p == self.st[0]) or (p == self.st[-1]):
            self.st.remove(p)
            return
        # 一定能够找到
        l = self.st.index(p)
        heappush(self.h, Region(self.st[l-1], self.st[l+1]))
        self.st.remove(self.st[l])

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)