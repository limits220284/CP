class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        n = len(coins)
        coins.sort()
        print(coins)
        # 能够添加出来二进制所有的位数
        ans = 0
        j = 0
        if coins[0] != 1:
            ans += 1
            j = 0
        else:
            j = 1
        x, y = 0, 1
        while j < n:
            if coins[j] + x > y + 1:
                ans += 1
                t = y + 1
                y = y + t
            else:
                y = y + coins[j]
                j += 1
            # print(x, y, ans)
            if y > target:
                return ans
        while y < target:
            ans += 1
            y = y + y + 1
        return ans