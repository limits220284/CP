class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = [c for c in str(n)]
        m = len(arr)
        i = m - 1
        while i > 0 and arr[i] <= arr[i - 1]:
                i -= 1
        if i == 0: return -1
        k = m - 1
        while k >= 0 and arr[k] <= arr[i - 1]:
                k -= 1
        MX = 2 ** 31 - 1
        arr[i - 1], arr[k] = arr[k], arr[i - 1]
        ans = arr[: i] + list(reversed(arr[i:]))
        ans = int("".join(ans))
        return ans if ans <= MX else -1
