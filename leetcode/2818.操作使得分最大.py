class Solution:
    def divide(self, n):
        i = 2
        ans = 0
        while i <= n // i:
            cnt = 0
            if n % i == 0:
                while n % i == 0:
                    n //= i
                    cnt += 1
                ans += 1
            i += 1
        if n > 1:
            ans += 1
        return ans
    
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        socre = []
        for num in nums:
            socre.append(self.divide(num))
        left = [0] * n
        right = [n] * n
        stk = []
        for i in range(n):
            while stk and socre[stk[-1]] < socre[i]:
                stk.pop()
            if not stk: left[i] = -1
            else: left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n-1, -1, -1):
            while stk and socre[stk[-1]] <= socre[i]:
                stk.pop()
            if not stk: right[i] = n
            else: right[i] = stk[-1]
            stk.append(i)
        arr = list(zip(deepcopy(nums), list(range(n))))
        arr.sort(reverse = True)
        ans = 1
        for x, idx in arr:
            cnt = (idx - left[idx]) * (right[idx] - idx)
            if cnt >= k:
                ans = ans * pow(x, k, MOD) % MOD
                k = 0
            else:
                ans = ans * pow(x, cnt, MOD) % MOD
                k -= cnt
            if k == 0: break
        return ans
        
        
        
        
        