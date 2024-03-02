class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        cnt = Counter()
        mx = -1
        candidate = -1
        self.arr = []
        for time, person in zip(times, persons):
            cnt[person] += 1
            if cnt[person] >= mx:
                mx = cnt[person]
                candidate = person
            self.arr.append((time, candidate))
        print(self.arr)
    def q(self, t: int) -> int:
        # 二分查找
        l, r = 0, len(self.arr)-1
        while l < r:
            mid = (l + r + 1) // 2
            if self.arr[mid][0] <= t:
                l = mid
            else:
                r = mid - 1
        return self.arr[l][1]
                


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)