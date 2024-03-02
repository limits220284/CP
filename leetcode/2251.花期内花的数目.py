class Solution:
    def fullBloomFlowers1(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # 如果start和end比较小，那么这题就可以采用差分数组来求解
        # 离散化也不行
        # 只能动态的维护某个时间点花的个数
        # 采用堆来实现
        # 将花按着右边端点进行排序，如果右边端点大于当前的人，直接弹出，否则就是当前堆中的个数
        n = len(people)
        arr = deepcopy(flowers)
        for i, p in enumerate(people):
            arr.append([p, inf])
        arr.sort()
        ans = [0] * n
        h = []
        cnt = Counter()
        for x, y in arr:
            if y == inf:
                while h and h[0] < x:
                    heappop(h)
                cnt[x] = len(h)
            else:
                heappush(h, y)
        for i in range(n):
            ans[i]= cnt[people[i]]
        return ans
    def fullBloomFlowers2(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # 排序+二分
        s = sorted([a for a, _ in flowers])
        e = sorted([a for _, a in flowers])
        ans = [0] * len(people)
        for i, p in enumerate(people):
            ans[i] = bisect_right(s, p) - bisect_left(e, p)
        return ans
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        diff = Counter()
        for start, end in flowers:
            diff[start] += 1
            diff[end + 1] -= 1
        times = sorted(diff.keys())
        ans = [0] * len(people)
        j = s = 0
        for p, i in sorted(zip(people, range(len(people)))):
            while j < len(times) and times[j] <= p:
                s += diff[times[j]]
                j += 1
            ans[i] = s
        return ans
        



















