class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        cnt = Counter(barcodes)
        cnt = list(cnt.items())
        print(cnt)
        cnt.sort(key = lambda x: (x[1]), reverse = True)
        print(cnt)
        arr = []
        for x, y in cnt:
            arr += [x] * y
        print(arr)
        ans = [0] * n
        for i in range((n + 1) // 2):
            ans[2 * i] = arr[i]
            if 2 * i + 1 < n:
                ans[2 * i + 1] = arr[i + (n + 1) // 2]
        return ans