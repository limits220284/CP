class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        n = len(supplies)
        arr = supplies[::]
        while len(arr) != n//2:
            x = -1
            mn = inf
            m = len(arr)
            for i in range(m-1):
                if arr[i] + arr[i+1] < mn:
                    mn = arr[i] + arr[i+1]
                    x = i
            arr = arr[:x] + [mn] + arr[x+2:]
        return arr