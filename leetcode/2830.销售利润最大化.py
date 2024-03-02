class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        # 动态规划
        # f[i]代表以i结尾的房子的最大值
        dic = defaultdict(list)
        for offer in offers:
            a, b, c = offer
            dic[b+1].append([a+1, b+1, c])
        # print(dic)
        f = [0] * (n+1)
        for i in range(1, n+1):
            arr = dic[i]
            # print(arr)
            for t in arr:
                f[i] = max(f[i], f[t[0]-1] + t[2])
            f[i] = max(f[i], f[i-1])
        # print(f)
        return max(f)