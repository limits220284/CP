class Solution:
    def reinitializePermutation(self, n: int) -> int:
        if n == 2:
            return 1
        step, pow2 = 1, 2
        while pow2 != 1:
            step += 1
            pow2 = pow2 * 2 % (n - 1)
        return step
