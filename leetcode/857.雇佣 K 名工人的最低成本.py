class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        qw = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])  # 按照 r 值排序
        h = [-q for q, _ in qw[:k]]  # 加负号变成最大堆
        heapify(h)
        sum_q = -sum(h)
        ans = sum_q * qw[k - 1][1] / qw[k - 1][0]  # 选 r 值最小的 k 名工人组成当前的最优解
        for q, w in qw[k:]:
            if q < -h[0]:  # sum_q 可以变小，从而可能得到更优的答案
                sum_q += heapreplace(h, -q) + q  # 更新堆顶和 sum_q
                ans = min(ans, sum_q * w / q)
        return ans