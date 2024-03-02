class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        qj = defaultdict(list)
        for i, x in enumerate(nums):
            qj[x].append(i)
        # print(qj)
        arr = []
        for k, v in qj.items():
            arr.append([v[0], v[-1]])
        # print(arr)
        # 合并区间
        arr.sort(key = lambda x: x[0])
        # print(arr)
        newarr = []
        i = 0
        while i < len(arr):
            if not newarr:
                newarr.append(arr[i])
            else:
                if arr[i][0] <= newarr[-1][1]:
                    newarr[-1][1] = max(newarr[-1][1], arr[i][1])
                else:
                    newarr.append(arr[i])
            i += 1
        # print(newarr)
        return pow(2, len(newarr) - 1, mod)
        
        
        